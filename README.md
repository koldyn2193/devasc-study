# devasc-study
Software Systems, Technologies and Security

Seminar on Software Systems, Technologies and Security
There are practical tasks about the following topics:
1. GitHub
2. Ansible
3. Docker
4. Jenkins
5. Unit testing
Required score to pass: 60/100
Create a README.md document in which you concisely document all the tasks using the following structure for each task:
● Task name => name of the task
● Task preparation => what preparation is necessary to perform the task? (short)
● Task implementation => what is the way you have implemented the task?
● Task troubleshooting => what were the problems encountered?
● Task verification => proof of the quality of the result (Screenshots)(Task1Screens)
At the end of the Skill exam, you will have all this information updated in the GitHub.
The details of the particular tasks are explained in the following pages.
Submission:
• Make your GitHub repo public and share its link with me using WebEx private message.
• Deadline: 26.09.2022 till 23:59 (St. Petersburg Time)




Task 1 -- GitHub Skills Test (25 points)
>Task name:
Manage GitHub scripts and documents
>Task description:
Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.

● The scripts you create in all the tasks will be copied into the repository “Skills2022” including the screenshots.
● Make sure that your local repository is connected to an online repository on GitHub (make your repository public so that I can evaluate the work, once you get the grades, you can make it private).
● After every step make sure that the local files are present on GitHub with a tag indicating the task name.
● Take screenshots indicating the success of your actions.
● At the end finalize the README.me file indicating the list of all the tasks and your remarks.

Preparations: 
apt-get update && upgrade
apt-get install git
####
create a github profile and a repository for this task
###
create directory for local git repo "skills2022"
### 
create a personal access token 

Imlementation:

![изображение](https://user-images.githubusercontent.com/44508549/192087944-bdad3101-9333-4392-b0f3-477cbd007b91.png)

![изображение](https://user-images.githubusercontent.com/44508549/192088483-701e3ac1-2ce4-4e48-8db7-ea057dbf566a.png)

![изображение](https://user-images.githubusercontent.com/44508549/192088550-1dde1ea3-433b-4729-9a12-cba5e15d4fe7.png)


Troubleshooting:
forgot about PAC, created one

Verification:

![изображение](https://user-images.githubusercontent.com/44508549/192091059-072495bc-d977-461a-8181-ecd41c1c2d91.png)

![изображение](https://user-images.githubusercontent.com/44508549/192091394-9d9d15a9-59f5-4c16-be04-91d5dc1f5b0c.png)



Task 2 -- Ansible Skills Test (20 points)
>Task name:
Manage WebServers through Ansible.
>Task description:
Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.
● Name the playbook WEBSERVER INSTALLATION AND TESTING.
● TWO tasks must be successful to get grade (Installation and Testing).
● Take screenshots indicating the success of your actions and save script files and related docs.


Preparations: 
systemctl start ssh
apt-get install openssh-server
apt-get install sshpass
apt-get install ansible

Imlementation:

add the following lines to the hosts file
[webservers]
192.0.2.3 ansible_ssh_user=devasc ansible_ssh_pass=Cisco123!

edit ansible.cfg file:
[defaults]
# Use local hosts file in this folder
inventory=./hosts
# Don't worry about RSA Fingerprints
host_key_checking = False 
# Do not create retry files
retry_files_enabled = False 



Troubleshooting:

Verification:
