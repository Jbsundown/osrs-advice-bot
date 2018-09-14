import tweepy
import random
from auths import *
from time import sleep

sleep_time = 7200
advice_file = 'tips.tsv'


class bot:
	def __init__(self, tips):
		self.tip_amount = self.load_tweets(tips)

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)
		self.api = tweepy.API(auth)

	def load_tweets(self,list):
		with open(list) as list_file:
			lines = list_file.readlines()
		return lines

	def tweet(self):
		tip = random.choice(self.tip_amount)

		try:
			#Used for debugging
			#print(tip)
			self.api.update_status(tip)

		except tweepy.TweepError as error:
			print(error.reason)

	def repeating(self, delay):
		while True:
			self.tweet()
			sleep(delay)

def main():
	robot = bot(advice_file)
	robot.repeating(sleep_time)

if __name__ == '__main__':
	main()
