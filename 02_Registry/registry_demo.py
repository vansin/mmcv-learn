from converters.converter1 import *

converter_cfg = dict(type='Converter1', a=1, b=2)
converter = CONVERTERS.build(converter_cfg)

print(converter)