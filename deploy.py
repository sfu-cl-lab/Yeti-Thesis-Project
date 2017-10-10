from subprocess import call

call(['npm','run','build'])
call(['rsync','-avzhe','ssh','dist/','hao@vul.haoxp.xyz:/home/hao/data_visualization'])
#call(['rsync','-avzhe','ssh','dist/static','root@haoxp.xyz:/usr/share/nginx/resume'])
#call(['firebase', 'deploy'])
