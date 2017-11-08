function curlx
	if not count $argv
echo "Please enter a URL"
else 
set splitlist (string split "/" $argv[1])
if ls $splitlist[(count $splitlist)]
echo "File already exists!"
else
curl $argv[1] > $splitlist[(count $splitlist)]
end
end
end
