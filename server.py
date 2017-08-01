#coding=utf-8
#+Author: Commoners
#+Email: a2550591@gmail.com
#+Date: <2017-07-27 星期四>
import eventlet
from eventlet import wsgi
from app import app

def Server(port):
    print "Server Started port:{0}".format(port)
    wsgi.server(eventlet.listen(("0.0.0.0",port)),
                app,log=open('server-{0}.log'.format(port),'a'),
                log_output=True,
                log_format='%(client_ip)s - -[%(date_time)s] "%(request_line)s" %(status_code)s %(body_length)s %(wall_seconds).6f'
                )
                
                

if __name__ == '__main__':
    #app.run(
    port = 5000
    Server(port)
