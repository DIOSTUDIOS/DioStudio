import multiprocessing


bind = '127.0.0.1:5050'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
thread = 5
proc_name = 'gunicorn.pid'
pidfile = 'gunicorn.pid'
accesslog = '/home/DioStudio/log/gunicorn_access.log'
daemon = True
