import poplib,time,re,os
 
try:
    client=poplib.POP3('pop.XXX.com',110) ## the pop3 sever address   
    client.user('mail_name') ## input the mail name
    client.pass_('mail_code') ## input the mail code
    config=client.stat()
except Exception:
    print 'Login Failure!!'
else:
    print 'Process Normal and Start Loop'
    time.sleep(5)
    
    while(1):
        client=poplib.POP3('pop.126.com',110)
        client.user('user_name')
        client.pass_('user_code')
        cur_config=client.stat()
        print cur_config
        if cur_config ==config:
            print 'Didn\'t receive new mail'  
        else:
            print 'Received {} new mail '.format(cur_config[0]-config[0]),
            flag=0
            for i in range(config[0]+1,cur_config[0]+1):
                status,msg,siz=client.top(i,0)
                print msg
                print '----------------------------------------'
                print status
                print '----------------------------------------'
                print siz
                if flag==1:
                    break
                for line in msg:
                    if re.match(r'^Subject: cs',line): ## if receiving a new mail, the subject is "Subject: cs", shutdown the computer
                        flag=1
                        break
            config=cur_config
            if flag==1:
                print 'that meet the requirement so turn off computer '
                os.system('shutdown -s -t 5')
            else:
                print 'that didn\'t meet the requirement! '
        time.sleep(30) ## every 30 ms to check whether a new mail has been received
