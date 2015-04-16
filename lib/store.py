import os
import redis

REDISTOGO_URL ='redis://redistogo:23712bcf49adcd0ebf95a130b59d4ed7@mummichog.redistogo.com:10196/'
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)