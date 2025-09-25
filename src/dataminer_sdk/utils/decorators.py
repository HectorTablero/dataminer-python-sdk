from functools import wraps


# Decorator to auto-generate async variants
def auto_async_methods(cls):
    for attr_name in dir(cls):
        if attr_name.startswith("_"):
            continue
        attr = getattr(cls, attr_name)
        if callable(attr) and "async_" not in attr_name:
            async_name = f"{attr_name}_async"

            async def async_method(self, *args, _sync_method=attr, **kwargs):
                kwargs["async_"] = True
                return await _sync_method(self, *args, **kwargs)

            setattr(cls, async_name, async_method)
    return cls
