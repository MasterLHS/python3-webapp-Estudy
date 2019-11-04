import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset="utf8", decode_responses=True)

r.set("15292151327", "123666")
#r.expire("mobile", 2)
import time
#time.sleep(2)
#print(r.get("mobile"))