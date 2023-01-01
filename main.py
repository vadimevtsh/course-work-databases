import redis
import hashlib

r = redis.Redis(host="localhost", port=6379, db=0)

"""
def schedule_row_cache(conn, row_id, delay):
	conn.zadd('delay:', row_id, delay)
	conn.zadd('schedule:', row_id, time.time())

def cache_rows(conn):
	while not QUIT:
		next = conn.zrange('schedule:', 0, 0, withscores=True)
		now = time.time()
		if not next or next[0][1] > now:
			time.sleep(.05)
			continue

		row_id = next[0][0]
		delay = conn.zscore('delay:', row_id)
		if delay <= 0:
			conn.zrem('delay:', row_id)
			conn.zrem('schedule:', row_id)
			conn.delete('inv:' + row_id)
			continue

		row = Inventory.get(row_id)
		conn.zadd('schedule:', row_id, now + delay)
		conn.set('inv:' + row_id, json.dumps(row.to_dict()))
"""
def check_token(conn, login):
	return conn.hget('login:', login) # fetch and return a given user, if available

def hash_password(password):
	hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
	return hashed_password

if __name__ == "__main__":
	print(hash_password("1234"))
	#r = redis.Redis(host="localhost", port=6379, db=0)