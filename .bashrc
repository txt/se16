mock() {
    root=$(git rev-parse --show-toplevel)
    if [ -d "$root" ]; then
       	(cd $root;
	 if [ ! -f Makefile ]; then
	     makefile0 > Makefile
	     git add Makefile
	 fi
       	 make $* ;)
    else
	echo "mock: nothing to do"
    fi
}