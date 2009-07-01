#! /usr/bin/env python
# http://biostumblematic.wordpress.com
# Accesses twitter statuses and outputs to a text file

# Change the following two lines with your credentials
user = 'username'
pw = 'password'

num_statuses = 5 # Changes number of statuses to show

import sys, os.path, twitter
api = twitter.Api(username=user, password=pw)

if sys.argv[1] == '-l':
    timeline = api.GetFriendsTimeline(user)
    i=0
    output = open(os.environ['HOME']+'/tweets.txt', 'w')  
    while i < num_statuses:
        output.write(timeline[i].user.name+'\n')
        output.write(timeline[i].text+'\n')
        output.write('\n')
        i+=1
    output.close()
        
elif sys.argv[1] == '-p':
    status = api.PostUpdate(sys.argv[2])
    print 'Twitter status updated'
    
else:
    print 'Invalid input'
    print 'Allowed options are:'
    print '-p (to post an update)'
    print '-l (to list friend statuses)'
    sys.exit(2)
