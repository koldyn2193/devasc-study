# devasc-study
## Software Systems, Technologies and Security

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




## Task 1 -- GitHub Skills Test (25 points)
>Task name:
Manage GitHub scripts and documents
>Task description:
Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.

● The scripts you create in all the tasks will be copied into the repository “Skills2022” including the screenshots.
● Make sure that your local repository is connected to an online repository on GitHub (make your repository public so that I can evaluate the work, once you get the grades, you can make it private).
● After every step make sure that the local files are present on GitHub with a tag indicating the task name.
● Take screenshots indicating the success of your actions.
● At the end finalize the README.me file indicating the list of all the tasks and your remarks.

### Preparations: 
apt-get update && upgrade
apt-get install git

create a github profile and a repository for this task

create directory for local git repo "skills2022"

create a personal access token 

### Imlementation:

![изображение](https://user-images.githubusercontent.com/44508549/192087944-bdad3101-9333-4392-b0f3-477cbd007b91.png)

![изображение](https://user-images.githubusercontent.com/44508549/192088483-701e3ac1-2ce4-4e48-8db7-ea057dbf566a.png)

![изображение](https://user-images.githubusercontent.com/44508549/192088550-1dde1ea3-433b-4729-9a12-cba5e15d4fe7.png)


### Troubleshooting:
forgot about PAC, created one

### Verification:

![изображение](https://user-images.githubusercontent.com/44508549/192091059-072495bc-d977-461a-8181-ecd41c1c2d91.png)

![изображение](https://user-images.githubusercontent.com/44508549/192091394-9d9d15a9-59f5-4c16-be04-91d5dc1f5b0c.png)



## Task 2 -- Ansible Skills Test (20 points)
>Task name:
Manage WebServers through Ansible.
>Task description:
Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.
● Name the playbook WEBSERVER INSTALLATION AND TESTING.
● TWO tasks must be successful to get grade (Installation and Testing).
● Take screenshots indicating the success of your actions and save script files and related docs.


### Preparations: 
systemctl start ssh
apt-get install openssh-server
apt-get install sshpass
apt-get install ansible

### Imlementation:

add the following lines to the hosts file
[webservers]
192.0.2.3 ansible_ssh_user=devasc ansible_ssh_pass=Cisco123!

edit ansible.cfg file:
[defaults]

inventory=./hosts

host_key_checking = False 

retry_files_enabled = False 


create an ansible playbook:


---
- hosts: webservers
  become: yes
  tasks:
   - name: INSTALL APACHE2
     apt: name=apache2 update_cache=yes state=latest
 
   - name: ENABLED MOD_REWRITE
     apache2_module: name=rewrite state=present
     notify:
       - RESTART APACHE2
 
   - name: APACHE2 LISTEN ON PORT 8081
     lineinfile: dest=/etc/apache2/ports.conf regexp="^Listen 80" line="Listen 8081" state=present
     notify:
       - RESTART APACHE2
 
   - name: APACHE2 VIRTUALHOST ON PORT 8081
     lineinfile: dest=/etc/apache2/sites-available/000-default.conf regexp="^<VirtualHost \*:80>" line="<VirtualHost *:8081>" state=present
     notify:
       - RESTART APACHE2
 
  handlers:
   - name: RESTART APACHE2
     service: name=apache2 state=restarted

- hosts: webservers
  become: yes
  tasks:
   - name: ping
     action: ping
     ignore_errors: true
   - name: curl
     shell: curl 192.0.2.3:8081     
     ignore_errors: true


start ansible playbook 
ansible-playbook -v playbook-apache-install.yaml

### Troubleshooting:
no apache services needed to be restarted after updates in configs, added handlers for that

### Verification:
in file output-task2


![изображение](https://user-images.githubusercontent.com/44508549/192143501-7aa06123-5a9b-451e-84a2-ee0a6ac7a13b.png)




## Task 3 -- Docker (25 points)
>Task name:
Manage Docker microservices
>Task description:
Create a docker microservice
● Create a docker “ntp service” (based on the information in the following urls)
● Adapt configuration elements according to your network context. ● Only a basic ntp server is required. Detailed ntp configuration elements are out of scope.
● Take screenshots indicating the success of your actions and save script files and related docs.
>Task source files:
Here is a selection of the many docker or GitHub webpages. URL:
https://hub.docker.com/r/ntpd/ntpd
https://github.com/linuxkit/linuxkit/blob/master/pkg/openntpd/Dockerfile https://hub.docker.com/r/cturra/ntp
https://github.com/cturra/docker-ntp
https://chrony.tuxfamily.org/faq.


### Preparations: 
apt-get install docker
apt-get install docker-compose
git clone https://github.com/cturra/docker-ntp

![изображение](https://user-images.githubusercontent.com/44508549/192144526-a3fa935d-7070-4fee-a9dd-08f753338d22.png)


### Imlementation:
docker-compose -d ntp

![изображение](https://user-images.githubusercontent.com/44508549/192144535-ab981fac-e8ea-48f3-aee0-48230c1e342c.png)

docker-compose logs ntp

![изображение](https://user-images.githubusercontent.com/44508549/192144580-6ba189d8-99ce-4603-80c6-dae3ddbfbddb.png)


### Troubleshooting:
change version in docker-compose.yaml to 3.3 instead of 3.9

### Verification:

![изображение](https://user-images.githubusercontent.com/44508549/192144699-2a1c8dfc-e756-46e1-93ea-92da3423729a.png)

![изображение](https://user-images.githubusercontent.com/44508549/192144802-99e1b74b-e355-4f5a-8671-ad40f7a7f7ab.png)


## Task 4 -- Jenkins (10 points)
>Task name:
CI/CD Pipeline using Jenkins
>Task description:
Create a Jenkins pipeline
● Create a Jenkins pipeline in which you download the necessary scripts and files from a GitHub repository and install the service from task 3 in a docker container.
● Take screenshots indicating the success of your actions and save script files.

Cant proceed, because not enough memory on pc to support vm with jenkins even with 6gb hard lags


## Task 5 -- Unit Testing (20 points)
>Task name:
Unit testing
>Task description:
Create a unittest script in Python that asserts the output of all the functions in the given Python module.
>Task execution:
● Complete the unit test for the given module. At least 3 out of 4 tests must be successful to get a score for this part.
● Take screenshots indicating the success of your actions and save script files in the repository.


Python Module: (save the code with any name of your choice)
```
def factors(n):
p = 2
f = list()
while n >= p*p :
if n % p == 0:
f.append(p)
n = int(n / p)
else:
p = p + 1
f.append(n)
return f
def is_prime(number):
if number <= 1:
return False
for n in range(2, number):
if number % n == 0:
return False
else:
return True
def vowels(text):
v = list()
for i in text:
if i in 'aeiouAEIOU':
v.append(i)
return v
#len() is builtin function to determine the length of a sequence. Write a unit test for len()
```

### Preparations: 
### Imlementation:
### Troubleshooting:
### Verification:
