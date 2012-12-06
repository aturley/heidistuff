import urllib2
import json

tweets = []

for page in range(1, 50):
    print "page =", page
    f = urllib2.urlopen('http://search.twitter.com/search.json?q=cat&include_entities=true&rpp=100&page=%d' % page)

    data = f.read()

    json_data = json.loads(data)
    these_tweets = json_data['results']
    
    tweets.extend(these_tweets)

    for tweet in these_tweets:
        if tweet['geo'] != None and tweet['entities'].has_key('urls') and len(tweet['entities']['urls']) > 0 and tweet['entities']['urls'][0]['display_url']:
            print tweet
            print tweet['geo']
            print tweet['entities']['urls'][0]['display_url']

print len(tweets)
