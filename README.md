oslo.config example
---------------------
- Tạo một group, tương ứng với 1 section trong file cấu hình
```
opt_simple_group = cfg.OptGroup(name='simple',
                                title='A simple example')
```

- Tạo các option, có thể là String, List, Dict ...
```
simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]
```
- Register an option group.

 An option group must be registered before options can be registered with the group.
```
CONF.register_group(opt_simple_group)
```
- Register an option schema.
```
CONF.register_opts(simple_opts, opt_simple_group)
```
- Use
```
print CONF.simple.enable
```
