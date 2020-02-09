
#!/bin/sh
if [ "$1" != "" ]; then
	curl -Ls -o /dev/null -w %{url_effective} $1 -D - | grep 'location' | cut -b 11-
else
	echo "you must provide an url argument"
fi
