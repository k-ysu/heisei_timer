import tweepy, time, sys
import random
from datetime import date

#argfile = str(sys.argv[1])

#特定日付コメント
specific_comment = {
  "20180503": "憲法記念日",
  "20180504": "みどりの日",
  "20180505": "こどもの日",
  "20180506": "ゴムの日",
  "20180509": "アイスクリームの日",
  "20180515": "沖縄復帰記念日",
  "20180527": "百人一首の日",
  "20180528": "花火の日",
  "20180716": "海の日",
  "20180811": "山の日",
  "20180815": "終戦記念日",
  "20180917": "敬老の日",
  "20180923": "秋分の日",
  "20181008": "体育の日",
  "20181103": "文化の日",
  "20181123": "勤労感謝の日",
  "20181223": "天皇誕生日",
}


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'KVBoxCZQdUEqgeVxIgFMQcYku'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'n7BxIejKJdsUR7raKO4YHp7jW8moLAW0ITWSOGjtjz8NF55ukV' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '976703244008222720-1KofTA3DyRUpKcyl7vDuCs42BkWEvW8'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'eqpzTYdTZdG2ZMh7oqeqKi9n5IlHdr1LS6DcGuGgsDkdv'#keep the quotes, replace thbis with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# End of Heisei
end_date = date(2019, 5, 1)
today = date.today()
#today = date(2018, 8, 15)
time_to_end = abs(end_date - today)
to_heisei = time_to_end.days

#Progress
progress = round ( (365-to_heisei) / 365 * 100)
number_of_thin = round( 24 * to_heisei / 365 )
number_of_thick = 24 - number_of_thin
progress_bar = "▓" * number_of_thick
progress_bar += "░" * number_of_thin

#specific_comment
key = "%04d%02d%02d" % ( today.year, today.month, today.day)
special_comment = ""
special_tag=""
if ( key in specific_comment ):
    special_comment += "今日は #平成最後の {}月{}日({})です。\n".format(today.month, today.day , specific_comment[key])
    special_tag = " #{} ".format(specific_comment[key])
else:
    special_comment += "今日は #平成最後の {}月{}日です。\n".format(today.month, today.day)


tweet = special_comment
tweet += "平成はあと" + str( time_to_end.days ) + "日です! \n"
tweet += "{} {}% \n".format(progress_bar, progress)
tweet += special_tag
tweet = tweet.encode('utf-8')

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
