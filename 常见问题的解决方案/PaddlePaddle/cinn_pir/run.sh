# 打开组合算子
export FLAGS_prim_enable_dynamic=true && export FLAGS_prim_all=true

# 打开 CINN 编译器相关 FLAG
export FLAGS_use_cinn=true
export FLAGS_cinn_new_group_scheduler=true
export FLAGS_group_schedule_tiling_first=true
export FLAGS_cinn_bucket_compile=true

# 打开 PIR 模式
export FLAGS_enable_pir_api=true

# 是否打印 Program IR 信息
export FLAGS_print_ir=true

python net.py
