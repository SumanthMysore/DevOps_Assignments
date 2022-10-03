#Run a git pull and compile for a project every week day at 9am and 3pm India time in a (CentOS/Rocky Linux) server on UTC time zone. Post a notification to Google Chat space once that compile is successful and if unsuccessful post a failure message.


git pull repo master
javac /home/sumaM/Devops\ BC/shell_assignment/sample.java
if [ $? -eq 0 ]
then 
	python3 /home/sumaM/Devops\ BC/shell_assignment/notification.py COMPILATION_SUCCESS
else
	python3 /home/sumaM/Devops\ BC/shell_assignment/notification.py COMPILATION_UNSUCCESSFUL
fi
