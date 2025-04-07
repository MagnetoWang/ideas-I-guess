
## Kaggle

### Kaggle - 入门
1. House Prices：https://www.kaggle.com/code/serigne/stacked-regressions-top-4-on-leaderboard
2. Kaggle写作质量比赛top1solution总结 - 匀速小子的文章 - 知乎 https://zhuanlan.zhihu.com/p/9711417764
3. Rohlik比赛复盘:top1 solution解读 - 匀速小子的文章 - 知乎 https://zhuanlan.zhihu.com/p/718323308
4. 高性能预测：https://www.kaggle.com/code/verracodeguacas/high-speed-predictions-no-gpu
5. 优秀人才
   1. Chris Deotte：https://www.kaggle.com/cdeotte


### Kaggle - 代码精读
1. https://www.kaggle.com/c/favorita-grocery-sales-forecasting/discussion/47582
2. fe高手：https://www.kaggle.com/plantsgo
3. nn高手：https://www.kaggle.com/kelexu
4. 融合高手：https://www.kaggle.com/yifanxie
5. 勤刷kernel和forum

### Kaggle - 工具
1. cuDF-Pandas：https://rapids.ai/cudf-pandas/

### Kaggle - 技巧，经验与思考
1. 经验
   1. 7次KDD Cup&Kaggle冠军的经验分享：https://tech.meituan.com/2022/01/06/7-kdd-cup-kaggle-automl.html
   2. 2024kddcupwhoiswho赛道top37solution - 匀速小子的文章 - 知乎 https://zhuanlan.zhihu.com/p/702394381
2. 技巧
   1. 偏差消除问题：https://tech.meituan.com/2020/08/20/kdd-cup-debiasing-practice.html



```


1.要不要在lgb模型的训练中使用early_stop?答:我的回答是不要。本次比赛的评估指标是对每个author单独计算auc值,然后加权。虽然比赛方提供的训练数据有14万条,但是具体到author只有700多个。如果用交叉验证,每折验证集的author只有100个左右,数据量太少了。这100个author无法代表真实世界中无穷无尽的样本,如果用这些样本评估而早停可能会欠拟合,所以我个人认为不要。
2.模型的训练过程中要不要使用加权,也就是用比赛的评估指标训练模型?答:经过实验发现效果并不好,我也思考了原因,通过对每个author的oof的auc作图后发现,一个author的论文数量越少,auc相对来说越低,甚至低于0.5,而论文数量越少错误的数量也会相对越少。因此,错误多的样本论文数量多,论文数量多的样本auc好,如果给auc好的样本大权重,auc差的样本小权重,明显是不合理的。最终还是选择不用加权来训练模型。
3.要不要使用模型融合?答:经过实验效果并不好,xgb和catboost效果比不上lgb模型,虽然模型融合线下oof提高了很多,但是提交上去还是不行,可能是线下选择blending权重的时候过拟合,最后还是选择只使用lgb模型。


```


## kaggle练习赛
1. 按照参与人数筛选：https://www.kaggle.com/competitions?sortOption=numTeams
2. 按照page：https://www.kaggle.com/competitions?listOption=completed&sortOption=recentlyClosed&page=4


### Mechanisms of Action (MoA) Prediction
1. SimpleNN：https://www.kaggle.com/competitions/lish-moa/discussion/201510

### Optiver - Trading at the Close
1. 1th place：https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/487446
2. 20th Place：https://www.kaggle.com/code/andrealunch/20th-place-submission
3. dnn：https://www.kaggle.com/code/juzehao/pytorch-dnn-e010c9
4. wide_deep：https://www.kaggle.com/code/usharengaraju/keras-saint-w-b
5. 模型
   1. CatBoost
   2. GRU
   3. Transformer
   4. GRU + Transformer
   5. CatBoost + GRU + Transformer

### UM
1. 1st：https://www.kaggle.com/competitions/um-game-playing-strength-of-mcts-variants/discussion/549801

### M5 Forecasting - Accuracy
1. https://www.kaggle.com/competitions/m5-forecasting-accuracy/leaderboard


### Home Credit - Credit Risk Model Stability
1. 1st：https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/discussion/508337
   1. https://www.kaggle.com/code/yuuniekiri/fork-of-home-credit-catboost-inference

### Home Credit Default Risk
1. https://www.kaggle.com/competitions/home-credit-default-risk/leaderboard

### IEEE-CIS Fraud Detection
1. 1st Place ：https://www.kaggle.com/competitions/ieee-fraud-detection/discussion/111308

### Backpack Prediction Challenge
1. 1st Place - Single Model - Feature Engineering：https://www.kaggle.com/competitions/playground-series-s5e2/discussion/565539
2. 特征思路：https://www.kaggle.com/competitions/playground-series-s5e2/discussion/563743
3. 机器资源
   1. My final solution is a single model trained with 500 features using 1xA100 GPU 80GB. However a single model with only 138 features trained with Kaggle's 1xT4 GPU 16GB also wins first place. I publish this simple Kaggle T4 GPU solution here.
   2. 1h 47m 4s · GPU T4 x2
4. 


#### 
```

```


### Kaggle - mercari-price-suggestion-challenge
```
比赛链接：https://www.kaggle.com/c/mercari-price-suggestion-challenge

解决方案：https://www.leiphone.com/category/yanxishe/HGSuMdM6c4U6jWLi.html

代码：https://github.com/pjankiewicz/mercari-solution

```

### Kaggle - Predict Future Sales
1. 1st：https://www.kaggle.com/code/kyakovlev/1st-place-solution-part-1-hands-on-data
2. https://www.kaggle.com/anqitu/feature-engineer-and-model-ensemble-top-10
3. https://www.kaggle.com/yuliagm/how-to-work-with-big-datasets-on-16g-ram-dask
4. 图形表达
   1. https://www.kaggle.com/dimitreoliveira/model-stacking-feature-engineering-and-eda
   2. https://www.kaggle.com/jagangupta/time-series-basics-exploring-traditional-ts
   3. https://www.kaggle.com/dlarionov/feature-engineering-xgboost
```
比赛链接：https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data

代码：https://www.kaggle.com/code/zhangyunsheng/xgboost/notebook

```





### Kaggle - Corporacion Favorita Grocery Sales Forecasting
1. solution
   1. https://www.kaggle.com/c/favorita-grocery-sales-forecasting/discussion/47544
2. 于是Corporación Favorita 向 Kaggle 社区提出了挑战，要求其建立一个可以准确预测商品销量的模型。Corporación Favorita 目前依靠主观预测来备份数据，很少通过自动化工具执行计划，他们非常期待通过机器学习实现在正确的时间提供足够正确的商品，来更好地让顾客满意。
```
比赛地址：

https://www.kaggle.com/c/favorita-grocery-sales-forecasting

论文地址：

https://arxiv.org/pdf/1803.04037.pdf

方案：https://cloud.tencent.com/developer/article/1166628
代码：https://www.kaggle.com/code/shixw125/1st-place-lgb-model-public-0-506-private-0-511/script
```


### Kaggle - PetFinder.my Adoption Prediction
1. 5th Place Solution Code：https://www.kaggle.com/code/bminixhofer/5th-place-solution-code


### Kaggle - Jane Street Real-Time Market Data Forecasting
1. Jane Street最新量化大赛金牌方案(含代码)：https://mp.weixin.qq.com/s/8mQkX3c17A_61A4CsZVxxA
   
```

https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/discussion/556542

代码:https://github.com/evgeniavolkova/kagglejanestreet/tree/master

https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/overview

```


### Kaggle - Elo Merchant Category Recommendation
1. 通过顾客的历史交易记录以及顾客和商家的信息数据进行模型训练，最终预测测试集里面所有信用卡的忠诚度分数。

### Kaggle - TalkingData AdTracking Fraud Detection Challenge



### Kaggle - March Machine Learning Mania 2025
1. https://www.kaggle.com/competitions/march-machine-learning-mania-2025

