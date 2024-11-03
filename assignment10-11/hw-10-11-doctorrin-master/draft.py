from functools import wraps

def custom_lru_cache(maxsize=128):
    cache = {}
    lru_order = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if args in cache:
                lru_order.remove(args)
                lru_order.append(args)
                return cache[args]

            result = func(*args)
            cache[args] = result
            lru_order.append(args)

            if len(cache) > maxsize:
                oldest = lru_order.pop(0)
                cache.pop(oldest)
            return result

        def cache_clear():
            nonlocal cache, lru_order
            cache.clear()
            lru_order.clear()
        wrapper.cache_clear = cache_clear
        return wrapper
    return decorator


