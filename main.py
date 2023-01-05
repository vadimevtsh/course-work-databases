import redis
import hashlib
import time

class MyRedis:
	def __init__(self, host_name="localhost", port=6379, db=0):
		self.r = redis.Redis(host_name, port, db)

	def update_token(self, login, password): # update user login info in the cache
		timestamp = time.time()
		time_to_live = 60 * 60 * 24
		self.r.setex(login, time_to_live, password)


	def check_token(self, login):
		return self.r.get(login) # fetch and return a given user, if available

	def hash_password(self, password): # hash user password using SHA-256 hashing algorithm
		hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		return hashed_password

	def get_all_entries(self): # not really implemented
		cursor = 0
		keys = []
		server_return = self.r.scan(cursor)
		print(server_return)



