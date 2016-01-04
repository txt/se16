url=se16.unbox.org

publish : typo 

typo: ready
	@- git status
	@- git commit -am "saving"
	@- git push origin master
	@- wget -O -  http://$(url)/update.cgi  	

commit: ready
	@- git status
	@- git commit -a
	@- git push origin master
	@- wget -O - http://$(url)/update.cgi

update: ready
	@- git pull origin master

status: ready
	@- git status

ready: readmes
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

readmes: project/README.html lectures/README.html

%/README.html : %/_etc/README.md
	./render.cgi $(subst .md,,$<) nohead > $@
	git add $@

setup:
	sudo pip install markdown pygments ispell
