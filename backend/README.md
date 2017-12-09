Can we make an effective spam filter using just term frequency and inverse document frequency?

Not sure what I am doing wrong here...

--

➜  ~
➜  ~ cd ~/src/py/meta
➜  meta git:(master) ✗ git remote -v
origin	git@github.com:kusl/flaskexperiment.git (fetch)
origin	git@github.com:kusl/flaskexperiment.git (push)
➜  meta git:(master) ✗ cd ~/src/py/meta/backend;
➜  backend git:(master) ✗ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  backend git:(master) ✗ git diff README.md
➜  backend git:(master) ✗ git diff README.md
➜  backend git:(master) ✗ cd ~/src/py/meta/backend;docker-compose build;docker-compose up;
backend_db uses an image, skipping
Building backend_app
Step 1/8 : FROM python:3.6
 ---> 79e1dc9af1c1
Step 2/8 : RUN apt-get update && apt-get -y install postgresql-client
 ---> Using cache
 ---> 39d07f8e32c2
Step 3/8 : RUN mkdir -p /var/www/backend
 ---> Using cache
 ---> 4c7a70996c36
Step 4/8 : WORKDIR /var/www/backend
 ---> Using cache
 ---> a328877188ca
Step 5/8 : ADD . /var/www/backend
 ---> 2b293ebf1b8b
Removing intermediate container dee4692e5dda
Step 6/8 : RUN pip install -r requirements.txt
 ---> Running in 71f2a5065efb
Collecting autopep8==1.3.3 (from -r requirements.txt (line 1))
  Downloading autopep8-1.3.3.tar.gz (108kB)
Collecting click==6.7 (from -r requirements.txt (line 2))
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
Collecting Flask==0.12.2 (from -r requirements.txt (line 3))
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
Collecting Flask-SQLAlchemy==2.3.2 (from -r requirements.txt (line 4))
  Downloading Flask_SQLAlchemy-2.3.2-py2.py3-none-any.whl
Collecting itsdangerous==0.24 (from -r requirements.txt (line 5))
  Downloading itsdangerous-0.24.tar.gz (46kB)
Collecting Jinja2==2.10 (from -r requirements.txt (line 6))
  Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
Collecting MarkupSafe==1.0 (from -r requirements.txt (line 7))
  Downloading MarkupSafe-1.0.tar.gz
Collecting psycopg2==2.7.3.2 (from -r requirements.txt (line 8))
  Downloading psycopg2-2.7.3.2-cp36-cp36m-manylinux1_x86_64.whl (2.7MB)
Collecting pycodestyle==2.3.1 (from -r requirements.txt (line 9))
  Downloading pycodestyle-2.3.1-py2.py3-none-any.whl (45kB)
Collecting SQLAlchemy==1.1.15 (from -r requirements.txt (line 10))
  Downloading SQLAlchemy-1.1.15.tar.gz (5.2MB)
Collecting Werkzeug==0.12.2 (from -r requirements.txt (line 11))
  Downloading Werkzeug-0.12.2-py2.py3-none-any.whl (312kB)
Building wheels for collected packages: autopep8, itsdangerous, MarkupSafe, SQLAlchemy
  Running setup.py bdist_wheel for autopep8: started
  Running setup.py bdist_wheel for autopep8: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/29/46/6d/658145e8419d7599a56d3398ef6b20f9bf865eeb35791d1625
  Running setup.py bdist_wheel for itsdangerous: started
  Running setup.py bdist_wheel for itsdangerous: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
  Running setup.py bdist_wheel for MarkupSafe: started
  Running setup.py bdist_wheel for MarkupSafe: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
  Running setup.py bdist_wheel for SQLAlchemy: started
  Running setup.py bdist_wheel for SQLAlchemy: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/2c/05/a6/b67f1ab4d5a08d3c3ad3edfc1e60e09f9263536aa3dc91824c
Successfully built autopep8 itsdangerous MarkupSafe SQLAlchemy
Installing collected packages: pycodestyle, autopep8, click, Werkzeug, itsdangerous, MarkupSafe, Jinja2, Flask, SQLAlchemy, Flask-SQLAlchemy, psycopg2
Successfully installed Flask-0.12.2 Flask-SQLAlchemy-2.3.2 Jinja2-2.10 MarkupSafe-1.0 SQLAlchemy-1.1.15 Werkzeug-0.12.2 autopep8-1.3.3 click-6.7 itsdangerous-0.24 psycopg2-2.7.3.2 pycodestyle-2.3.1
 ---> bc5e2db590c0
Removing intermediate container 71f2a5065efb
Step 7/8 : EXPOSE 5000
 ---> Running in 4e6b4a911b09
 ---> 28e0fd441bd3
Removing intermediate container 4e6b4a911b09
Step 8/8 : CMD python backend.py
 ---> Running in 83701f0c4cd7
 ---> 0f5caf77e932
Removing intermediate container 83701f0c4cd7
Successfully built 0f5caf77e932
Starting backend_backend_db_1 ...
Starting backend_backend_db_1 ... done
Recreating backend ...
Recreating backend ... done
Attaching to backend_backend_db_1, backend
backend_db_1   | 2017-12-09 12:47:59.646 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
backend_db_1   | 2017-12-09 12:47:59.646 UTC [1] LOG:  listening on IPv6 address "::", port 5432
backend_db_1   | 2017-12-09 12:47:59.653 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
backend_db_1   | 2017-12-09 12:47:59.679 UTC [24] LOG:  database system was shut down at 2017-12-09 12:44:38 UTC
backend_db_1   | 2017-12-09 12:47:59.696 UTC [1] LOG:  database system is ready to accept connections
backend        | /usr/local/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
backend        |   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
backend        |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
backend        |  * Restarting with stat
backend        | /usr/local/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
backend        |   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
backend        |  * Debugger is active!
backend        |  * Debugger PIN: 234-347-101
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET / HTTP/1.1" 500 -
backend        | Traceback (most recent call last):
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1997, in __call__
backend        |     return self.wsgi_app(environ, start_response)
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1985, in wsgi_app
backend        |     response = self.handle_exception(e)
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1540, in handle_exception
backend        |     reraise(exc_type, exc_value, tb)
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/_compat.py", line 33, in reraise
backend        |     raise value
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1982, in wsgi_app
backend        |     response = self.full_dispatch_request()
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1614, in full_dispatch_request
backend        |     rv = self.handle_user_exception(e)
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1517, in handle_user_exception
backend        |     reraise(exc_type, exc_value, tb)
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/_compat.py", line 33, in reraise
backend        |     raise value
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1612, in full_dispatch_request
backend        |     rv = self.dispatch_request()
backend        |   File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1598, in dispatch_request
backend        |     return self.view_functions[rule.endpoint](**req.view_args)
backend        |   File "/var/www/backend/backend.py", line 19, in hello_world
backend        |     create_message()
backend        |   File "/var/www/backend/backend.py", line 54, in create_message
backend        |     shared.db.session.commit()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/scoping.py", line 157, in do
backend        |     return getattr(self.registry(), name)(*args, **kwargs)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 921, in commit
backend        |     self.transaction.commit()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 461, in commit
backend        |     self._prepare_impl()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 441, in _prepare_impl
backend        |     self.session.flush()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 2192, in flush
backend        |     self._flush(objects)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 2312, in _flush
backend        |     transaction.rollback(_capture_exception=True)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/langhelpers.py", line 66, in __exit__
backend        |     compat.reraise(exc_type, exc_value, exc_tb)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/compat.py", line 187, in reraise
backend        |     raise value
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 2276, in _flush
backend        |     flush_context.execute()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/unitofwork.py", line 389, in execute
backend        |     rec.execute(self)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/unitofwork.py", line 548, in execute
backend        |     uow
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/persistence.py", line 156, in save_obj
backend        |     base_mapper, states, uowtransaction
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/persistence.py", line 279, in _organize_states_for_save
backend        |     states):
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/persistence.py", line 1105, in _connections_for_states
backend        |     connection = uowtransaction.transaction.connection(base_mapper)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 294, in connection
backend        |     return self._connection_for_bind(bind, execution_options)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 392, in _connection_for_bind
backend        |     conn = self._parent._connection_for_bind(bind, execution_options)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 403, in _connection_for_bind
backend        |     conn = bind.contextual_connect()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/base.py", line 2112, in contextual_connect
backend        |     self._wrap_pool_connect(self.pool.connect, None),
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/base.py", line 2151, in _wrap_pool_connect
backend        |     e, dialect, self)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/base.py", line 1465, in _handle_dbapi_exception_noconnection
backend        |     exc_info
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/compat.py", line 203, in raise_from_cause
backend        |     reraise(type(exception), exception, tb=exc_tb, cause=cause)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/compat.py", line 186, in reraise
backend        |     raise value.with_traceback(tb)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/base.py", line 2147, in _wrap_pool_connect
backend        |     return fn()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 387, in connect
backend        |     return _ConnectionFairy._checkout(self)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 766, in _checkout
backend        |     fairy = _ConnectionRecord.checkout(pool)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 516, in checkout
backend        |     rec = pool._do_get()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 1138, in _do_get
backend        |     self._dec_overflow()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/langhelpers.py", line 66, in __exit__
backend        |     compat.reraise(exc_type, exc_value, exc_tb)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/util/compat.py", line 187, in reraise
backend        |     raise value
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 1135, in _do_get
backend        |     return self._create_connection()
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 333, in _create_connection
backend        |     return _ConnectionRecord(self)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 461, in __init__
backend        |     self.__connect(first_connect_check=True)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/pool.py", line 651, in __connect
backend        |     connection = pool._invoke_creator(self)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/strategies.py", line 105, in connect
backend        |     return dialect.connect(*cargs, **cparams)
backend        |   File "/usr/local/lib/python3.6/site-packages/sqlalchemy/engine/default.py", line 393, in connect
backend        |     return self.dbapi.connect(*cargs, **cparams)
backend        |   File "/usr/local/lib/python3.6/site-packages/psycopg2/__init__.py", line 130, in connect
backend        |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
backend        | sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused
backend        | 	Is the server running on host "localhost" (::1) and accepting
backend        | 	TCP/IP connections on port 5432?
backend        | could not connect to server: Connection refused
backend        | 	Is the server running on host "localhost" (127.0.0.1) and accepting
backend        | 	TCP/IP connections on port 5432?
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=jquery.js HTTP/1.1" 200 -
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1" 200 -
backend        | 172.20.0.1 - - [09/Dec/2017 12:49:30] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -


--

However, when I run psql, it works completely fine

➜  backend git:(master) ✗ psql -h localhost -U dbadmin
Password for user dbadmin:
psql (9.6.6, server 10.1)
WARNING: psql major version 9.6, server major version 10.
         Some psql features might not work.
Type "help" for help.

dbadmin=#




