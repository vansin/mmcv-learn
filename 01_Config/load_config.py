from mmcv import Config

# 基础配置
cfg1 = Config.fromfile('config_a.py')
print(cfg1)

# 不含重复键值从基类配置文件继承
cfg2 = Config.fromfile('config_b.py')
print(cfg2)

cfg3 = Config.fromfile('config_c.py')
print(cfg3)

cfg4 = Config.fromfile('config_d.py')
print(cfg4)

cfg5 = Config.fromfile('config_e.py')
print(cfg5)

cfg6 = Config.fromfile('config_f.py')
print(cfg6)

cfg7 = Config.fromfile('config_g.py')
print(cfg7)

