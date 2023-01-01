import redis
import hashlib
import time

class MyRedis:
	def __init__(self, host_name="localhost", port=6379, db=0):
		self.r = redis.Redis(host_name, port, db)

	def update_token(self, login, password): # update user login info in the cache
		timestamp = time.time()
		self.r.hset('login:', login, password)


	def check_token(self, login):
		return self.r.hget('login:', login) # fetch and return a given user, if available

	def hash_password(self, password): # hash user password using SHA-256 hashing algorithm
		hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		return hashed_password


