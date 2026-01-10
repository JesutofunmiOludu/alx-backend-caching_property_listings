from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)


def get_all_properties():
    propertie = cache.get('all_properties')

    if propertie is None:

        propertie = list(Property.objects.all())

        cache.set('all_properties', propertie, 36000)

        return propertie


def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio
        }

        logger.info(f"Redis cache metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Failed to retrieve Redis metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0
        }








