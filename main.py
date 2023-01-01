import redis
import hashlib

class MyRedis:
	def __init__(self, host_name="localhost", port=6379, db=0)
	self.r = redis.Redis(host_name, port, db)

	def update_token(login, password): # update user login info in the cache
		timestamp = time.time()
		r.hset('login:', login, password)
		r.zadd('recent:', login, timestamp)


	def check_token(login):
		return r.hget('login:', login) # fetch and return a given user, if available

	def hash_password(password): # hash user password using SHA-256 hashing algorithm
		hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		return hashed_password