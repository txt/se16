url="http://withglee.org"

publish : typo updatecgi

updatecgi:
	@- wget -O -  http://withglee.org/update.cgi  > /dev/null

typo: ready
	@- git status
	@- git commit -am "saving"
	@- git push origin master 
	- echo 111
        - echo "wget -O - $(url)/update.cgi"
        wget -O - $(url)/update.cgi

commit: ready
	@- git status
	@- git commit -a
	@- git push origin master
        @- wget -O - $(url)/update.cgi

update: ready
	@- git pull origin master

status: ready
	@- git status

ready:
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

