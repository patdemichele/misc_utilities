function maxcurl
    if not count $argv
        echo "Please enter a URL"
    else
        for url in (curl $argv[1] | string match -r "\"[\w\-/\.:]*.pdf\"")
            set urlx (string replace --all "\"" "" $url)
	        if string match -r "https?://" $urlx
	            curlx $urlx
	        else
	            echo "TODO: work on relative paths"
	        end
        end
    end
end