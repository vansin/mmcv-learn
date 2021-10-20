from mmcv import Config

# 基础配置
cfg1 = Config.fromfile('config_a.py')
print(cfg1)

# 不含重复键值从基类配置文件继承
cfg2 = Config.fromfile('config_b.py')
print(cfg2)

# 含重复键值对从基类配置文件继承
cfg3 = Config.fromfile('config_c.py')
print(cfg3)

# 从具有忽略字段的配置文件继承
cfg4 = Config.fromfile('config_d.py')
print(cfg4)

# 从多个基类配置文件继承（基类配置文件不应包含相同的键）
cfg5 = Config.fromfile('config_e.py')
print(cfg5)

# 您可以使用以下语法引用在基类中定义的变量。
cfg6 = Config.fromfile('config_f.py')
print(cfg6)

# 从基类引用变量
cfg7 = Config.fromfile('config_g.py')
print(cfg7)

