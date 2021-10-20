from mmcv.utils import Registry
# 创建转换器（converter）的注册器（registry）
# CONVERTERS = Registry('converter')

# 创建一个构建函数
def build_converter(cfg, registry, *args, **kwargs):
    cfg_ = cfg.copy()
    converter_type = cfg_.pop('type')
    if converter_type not in registry:
        raise KeyError(f'Unrecognized converter t ype {converter_type}')
    else:
        converter_cls = registry.get(converter_type)

    converter = converter_cls(*args, **kwargs, **cfg_)
    return converter

# 创建一个用于转换器（converters）的注册器，并传递（registry）``build_converter`` 函数
CONVERTERS = Registry('converter', build_func=build_converter)