import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
# r.set('foo', 'bar')
 
# r.get('foo')

r.incrby('sr-60888-2024-08-08',1)
print(r.get('sr-60888-2024-08-08'))
