from jeeves.conf import settings
from jeeves.utils import importlib

BACKENDS = {
    'memcached': 'memcached',
    'localmem': 'localmem',
}

def get_cache(backend):
    if backend == 'Default':
        backend = settings.CACHE_BACKEND

    if not backend:
        return None

    mod_path, cls_name = backend.rsplit('.', 1)
    mod = importlib.import_module(mod_path)
    backend_cls = getattr(mod, cls_name)

    cache = backend_cls(settings.CACHE_LOCATION, {'params': {'timeout': settings.CACHE_DEFAULT_TIMEOUT}})

    return cache

cache = get_cache(backend='Default')
