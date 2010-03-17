.DEFAULT_GOAL = development
.PHONY = development clean

bootstrap.py :
	wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

bin/buildout : bootstrap.py
	python bootstrap.py

development : bin/buildout
	./bin/buildout

clean :
	rm -rf bin src share lib build include develop-eggs eggs parts .installed.cfg downloads bootstrap.py *-log.txt
