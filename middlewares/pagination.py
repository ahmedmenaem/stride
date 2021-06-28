from functools import wraps

def pagination_middleware():
    def _pagination_decorator(f):
        @wraps(f)
        def __pagination_decorator(*args, **kwargs):
            # print(request)
            print('before home')
            result = f(*args, **kwargs)
            print(*args)
            print('home result: %s' % result)
            print('after home')
            return result
        return __pagination_decorator
    return _pagination_decorator

