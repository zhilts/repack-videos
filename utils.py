from functools import wraps

__all__=[
    "wrap_result",
]


def wrap_result(wrapper_fn):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            result = fn(*args, **kwargs)
            return wrapper_fn(result)
        return decorator
    return wrapper
