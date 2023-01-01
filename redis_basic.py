import redis

r = redis.Redis(host='localhost', port=6379)
for i in r.lrange('names', 0, -1):
    print(i.decode())
