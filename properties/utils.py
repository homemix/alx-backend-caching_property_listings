import logging

from django.core.cache import cache
from django_redis import get_redis_connection

from properties.models import Property

logger = logging.getLogger(__name__)
def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values(
            'id', 'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
    return properties


def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = (hits / total) if total else None

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": round(hit_ratio, 2) if hit_ratio is not None else "N/A"
    }

    logger.info(f"Redis Metrics: Hits={hits}, Misses={misses}, Hit Ratio={metrics['hit_ratio']}")
    return metrics
