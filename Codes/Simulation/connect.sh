#Connect to proxy
# To prove connectivity type "curl -D- -o /dev/null -s http://www.google.com", if there is a response, there is a connection to web
echo "Digit your username and passwd, else, type cancel in username"
echo
read -p "Enter Username: " a
if [ "$a" != "cancel" ]
then
read -s -p "Enter Password: " b
http_proxy="http://"$a":"$b"@proxyapp.unal.edu.co:8080/"
export http_proxy=$http_proxy
export https_proxy=$http_proxy
http_proxy=''
echo "Always that you will use sudo, do it as 'sudo -E' to import proxies"
echo
fi
