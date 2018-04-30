import tweepy, time, sys
import random

#argfile = str(sys.argv[1])


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'KVBoxCZQdUEqgeVxIgFMQcYku'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'n7BxIejKJdsUR7raKO4YHp7jW8moLAW0ITWSOGjtjz8NF55ukV' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '976703244008222720-1KofTA3DyRUpKcyl7vDuCs42BkWEvW8'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'eqpzTYdTZdG2ZMh7oqeqKi9n5IlHdr1LS6DcGuGgsDkdv'#keep the quotes, replace thbis with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)





#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#lines = open(argfile,'r').read().splitlines()
#myline =random.choice(lines)
#tweet = myline + "  " + random.choice(tags)+ "  " + random.choice(tags)
tweet = 'This is Test ' + str( random.randint(1, 100) )
print(tweet)
api.update_status(tweet)


#for line in f:
#    tweet=line+str(random.randrange(1000))
#    print (tweet)
#    print line
#    api.update_status(tweet)
#    print ("done")
#    time.sleep(180)#Tweet every 15 minutes
