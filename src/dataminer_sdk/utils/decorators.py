# Decorator to auto-generate async variants
def auto_async_methods(cls):
    """
    Class decorator that automatically generates asynchronous variants
    of synchronous methods.

    For each callable attribute of the class that does not start with an
    underscore (`_`) and does not already contain `"async_"` in its name,
    this decorator creates a new method with the suffix `"_async"`.  

    The generated async method calls the original synchronous method with
    the same arguments, but forces the keyword argument `async_ = True`.

    Example:
        >>> @auto_async_methods
        ... class MyService:
        ...     def fetch(self, x: int, async_: bool = False):
        ...         return x * 2 if not async_ else x * 3
        ...
        >>> svc = MyService()
        >>> svc.fetch(2)
        4
        >>> await svc.fetch_async(2)
        6

    Args:
        cls (type): The class to decorate.

    Returns:
        type: The same class, augmented with async method variants.
    """
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
