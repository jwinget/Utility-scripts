#!/usr/bin/env python
# http://biostumblematic.wordpress.com

import sys, string
from pysqlite2 import dbapi2 as sqlite

scriptdir = '/home/jason/scripts/'

def taskadd():
    connection = sqlite.connect(scriptdir+'tasks.db')
    cursor = connection.cursor()
    # Creating a new task
    newtask = raw_input('What do you need to do? >> ')
    t = (newtask,)
    cursor.execute('insert into task_list values (NULL, ?, date("now"), "False")', t)
    connection.commit()
    cursor.close()

def taskcomplete():
    connection = sqlite.connect(scriptdir+'tasks.db')
    cursor = connection.cursor()
    completedtask = input('ID of completed task >> ')
    cursor.execute('update task_list set completion = "True" where task_id ='+str(completedtask))
    connection.commit()
    cursor.close
            
def todayToDo():
    connection = sqlite.connect(scriptdir+'tasks.db')
    cursor = connection.cursor()
    # Write today's tasks
    cursor.execute('select * from task_list where completion="False"')
    todaystasks=[]
    i = 1
    for row in cursor:
        todaystasks.append(str(i)+': '+row[1]+' (ID: '+str(row[0])+')\n')
        i += 1
    output = open(scriptdir+'todaystasks.txt', 'w')    
    output.writelines(todaystasks)
    output.close()
    cursor.close()

action = 0
while action != 3:        
    print 'What do you want to do?'
    print '1. Add a new task'
    print '2. Complete a task'
    print '3. Prepare the task list & quit'
    action = input('>> ')
    if action == 1:
        taskadd()
    elif action == 2:
        taskcomplete()
else:
    todayToDo()
    sys.exit()

