## Paddle
1. 竞赛：https://aistudio.baidu.com/competition




### 广告生成式序列化推荐算法优化
1. https://aistudio.baidu.com/competition/detail/1305/0/introduction


### 广告视频生成推理性能优化
1. https://aistudio.baidu.com/competition/detail/1307/0/introduction


### 搜索场景广告视频AIGC产品优化
1. https://aistudio.baidu.com/competition/detail/1309/0/introduction


### 广告图片描述生成
1. https://aistudio.baidu.com/competition/detail/1190/0/introduction

### 基于大模型的广告检索
1. https://aistudio.baidu.com/competition/detail/1188/0/introduction


### CUDA Topk 题解和优化
1. https://aistudio.baidu.com/competition/detail/1095/0/introduction

### 基于向量交集的TopK搜索
1. https://aistudio.baidu.com/competition/detail/1046/0/introduction

### 搜索答案组织
1. https://aistudio.baidu.com/competition/detail/1044/0/introduction

### AIGC推理性能优化
1. https://aistudio.baidu.com/competition/detail/913/0/task-definition

### 商业转化行为预测
1. https://aistudio.baidu.com/competition/detail/877/0/introduction

### 基于用户行为和商品属性的购买商品预测
1. https://aistudio.baidu.com/competition/detail/914/0/task-definition
2. 用户和产品特征构建：https://aistudio.baidu.com/projectdetail/438772?searchKeyword=%E5%9F%BA%E4%BA%8E%E7%94%A8%E6%88%B7%E8%A1%8C%E4%B8%BA%E5%92%8C%E5%95%86%E5%93%81%E5%B1%9E%E6%80%A7%E7%9A%84%E8%B4%AD%E4%B9%B0%E5%95%86%E5%93%81%E9%A2%84%E4%BC%B0&searchTab=ALL

## 入门赛
### 个贷违约预测
1. https://aistudio.baidu.com/competition/detail/803/0/introduction
2. 方案
   1. https://aistudio.baidu.com/projectdetail/3555696?channelType=0&channel=0
   2. 对于样本不平衡的问题，修改损失函数的权重，将负样本的权重设为0.2，正样本为1.0
   3. 对于连续数值型变量，对他们进行 均值-方差归一化
   4. 对于分类变量，在网络中进行重编码（即增加一个全连接层，用于模拟embedding）
   5. 本方案直接弃用了地区编码，时间等信息。
3. 模型结构
   1. 更替网络结构：当前的网络仅包含4个全连接层和一个Sigmoid函数，较为简朴，可以增加层数和激活函数促使模型收敛到更高精度。
   2. 对时间信息等加以使用。
   3. 使用dropout等策略。




#### 数据处理
1. 返回数值型和非数值型，以及label
```python
class MyDateset(paddle.io.Dataset):
    # csv_dir对应要读取的数据地址，standard_csv_dir用于生成均值和方差信息对数据进行归一化的文件地址
    def __init__(self,csv_dir,standard_csv_dir='data/data130186/train_public.csv',mode = 'train'):
        super(MyDateset, self).__init__()

        # 读取数据
        self.df = pd.read_csv(csv_dir)
        
        # 构造各个变量的均值和方差
        st_df = pd.read_csv(standard_csv_dir)
        self.mean_df = st_df.mean()
        self.std_df = st_df.std()

        # 分别指定数值型变量/分类变量/不使用的变量
        self.num_item = ['total_loan', 'year_of_loan', 'interest','monthly_payment',
        'debt_loan_ratio', 'del_in_18month', 'scoring_low','scoring_high', 'known_outstanding_loan', 'known_dero','pub_dero_bankrup', 'recircle_b', 'recircle_u', 
        'f0', 'f1','f2', 'f3', 'f4', 'early_return', 'early_return_amount','early_return_amount_3mon']
        self.un_num_item = ['class','employer_type','industry','work_year','house_exist', 'censor_status',
        'use',
        'initial_list_status','app_type',
        'policy_code']
        self.un_use_item = ['loan_id', 'user_id',
        'issue_date', 
        'post_code', 'region',
        'earlies_credit_mon','title']

        # 构造一个映射表，将分类变量/分类字符串映射到对应数值上
        un_num_item_list = {}
        for item in self.un_num_item:
            un_num_item_list[item]=list(set(st_df[item].values))
        self.un_num_item_list = un_num_item_list

        self.mode = mode

    def __getitem__(self, index):
        data=[]

        # 进行归一化，如果这个数值缺省了直接设置为0
        for item in self.num_item:
            if np.isnan(self.df[item][index]):
                data.append((0-self.mean_df[item])/self.std_df[item])
            else:
                data.append((self.df[item][index]-self.mean_df[item])/self.std_df[item])
        
        emb_data = []

        # 将分类变量映射到对应数值上
        for item in self.un_num_item:
            try:
                if self.df[item][index] not in self.un_num_item_list[item]:
                    emb_data.append(-1)
                else:
                    emb_data.append(self.un_num_item_list[item].index(self.df[item][index]))
            except:
                emb_data.append(-1)

        data = paddle.to_tensor(data).astype('float32')
        emb_data = paddle.to_tensor(emb_data).astype('float32')

        # 如果当前模式不为train，则返回对应的loan_id，用于锁定样本条目
        if self.mode == 'train':
            label = self.df['isDefault'][index]
        else:
            label = self.df['loan_id'][index]

        label = np.array(label).astype('int64')
        return data,emb_data,label

    def __len__(self):
        return len(self.df)

```


#### 模型结构
1. 交叉熵可以控制正负样本计算
```python

class MyNet(paddle.nn.Layer):
    def __init__(self):
        super(MyNet,self).__init__()
        self.fc = paddle.nn.Linear(in_features=21, out_features=512)

        self.emb1 = paddle.nn.Linear(in_features=10,out_features=2048)
        self.emb2 = paddle.nn.Linear(in_features=2048,out_features=512)

        self.out = paddle.nn.Linear(in_features=1024,out_features=2)

    def forward(self,data,emb_data):
        x = self.fc(data)

        emb = self.emb1(emb_data)
        emb = self.emb2(emb)

        x = paddle.concat([x,emb],axis=-1)

        x = self.out(x)
        
        x = paddle.nn.functional.sigmoid(x)
        return x


```


### 英雄联盟大师预测
1. https://aistudio.baidu.com/competition/detail/797/0/introduction



### 产品评论观点提取
1. https://aistudio.baidu.com/competition/detail/802/0/task-definition


### 吃鸡排名预测挑战赛
1. https://aistudio.baidu.com/competition/detail/799/0/related-material

```



```


### 手机行为识别
1. https://aistudio.baidu.com/competition/detail/798/0/leaderboard
2. https://aistudio.baidu.com/projectdetail/3979175

```



```


### MarTech Challenge 用户购买预测
1. https://aistudio.baidu.com/competition/detail/819/0/related-material
2. 时间特征：https://aistudio.baidu.com/projectdetail/438793
```



```


### MarTech Challenge 点击反欺诈预测
1. https://aistudio.baidu.com/competition/detail/818/0/introduction
2. https://aistudio.baidu.com/projectdetail/3035909?channelType=0&channel=0
```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```


### 

```



```

