import tweepy, time, sys
import random
from datetime import date

#argfile = str(sys.argv[1])


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'KVBoxCZQdUEqgeVxIgFMQcYku'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'n7BxIejKJdsUR7raKO4YHp7jW8moLAW0ITWSOGjtjz8NF55ukV' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '976703244008222720-1KofTA3DyRUpKcyl7vDuCs42BkWEvW8'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'eqpzTYdTZdG2ZMh7oqeqKi9n5IlHdr1LS6DcGuGgsDkdv'#keep the quotes, replace thbis with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# End of Heisei
end_date = date(2019, 4, 30)
today = today = date.today()
time_to_end = abs(end_date - today)
to_heisei = time_to_end.days
#to_heisei = 320

#Progress

progress = round ( (365-to_heisei) / 365 * 100)
number_of_thin = round( 24 * to_heisei / 365 )
number_of_thick = 24 - number_of_thin
progress_bar = "▓" * number_of_thick
progress_bar += "░" * number_of_thin


tweet = "今日は平成最後の{}月{}日です \n".format(today.month, today.day)
tweet += "平成はあと" + str( time_to_end.days ) + "日です! \n"

tweet += "{} {}%".format(progress_bar, progress)

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#lines = open(argfile,'r').read().splitlines()
#myline =random.choice(lines)
#tweet = myline + "  " + random.choice(tags)+ "  " + random.choice(tags)
#tweet = 'This is Test ▓░' + str( random.randint(1, 100) )
print(tweet)
api.update_status(tweet)


#for line in f:
#    tweet=line+str(random.randrange(1000))
#    print (tweet)
#    print line
#    api.update_status(tweet)
#    print ("done")
#    time.sleep(180)#Tweet every 15 minutes
