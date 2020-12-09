# Narvan API

This web service is provided to calculate Ackermann function,The nth sentence of the Fibonacci sequence and Factorial function.
Git Flow Feature branch is used to manage Git and Travis-ci is used for the continuous integration of the project.
The Travis-ci is connected to Git's Ropositories and after every push,project starts to run on travis-ci's own servers according to configurations in .travis.yml 
and all its unit tests are checked automatically.
also,Git work flow is used to manage branches.

## Installation

#### to install follow the steps below:

1. #### Clone repository. use this command:

```
git clone https://github.com/MohammadReza-Jafari/narvan.git
```

2. #### Go to root of project
```
cd narvan
```

3. #### Install venv

```
python -m venv virtual
```

4. #### activate venv

- to activate on windows machines use the following command:

```
.\virtual\Scripte\activate
```

- and for other operation systems see [Python Documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

5. #### install packages
```
pip install -r requirements.txt
```



## Usage
#### to make use of project follow the steps below:

1. #### make migrations
```
python manage.py makemigrations
```

2. #### migrate
```
python manage.py migrate
```

3. #### create a superuser
```
python manage.py createsuperuser
```

4. #### run django server
```
python manage.py runserver
```

on [narvan api doc](http://127.0.0.1:8000/api/doc/) you can visit api documentation and see how to use every services.
to test this api you can see [narvan api doc](http://127.0.0.1:8000/api/doc/) that created by swagger and test services or go to any of following urls
and make post requests with specified value:

* [Fibonacci](http://127.0.0.1:8000/api/calculate/fibonacci)
   * method=post | reques-body = { “n”: An Integer value}


* [Factorial](http://127.0.0.1:8000/api/calculate/factorial)
   * method=post | reques-body = { “n”: An Integer value}

* [Ackermann](http://127.0.0.1:8000/api/calculate/ackermann)
   * method=post reques-body ={“m”: An Integer value, “n”: An Integer value}


##### for system monitoring you can just open log.txt in Reports directory inside project root and see details of every successful request <br />
![log.txt](https://github.com/MohammadReza-Jafari//pysru_bot/blob/master/3.png?raw=true) <br />

##### or by the created user in previous steps enter admin site of django and see the reports table there. <br/>
![log.txt](https://github.com/MohammadReza-Jafari//pysru_bot/blob/master/2.png?raw=true) <br />


## Author
#### Mohammad Reza Jafari

## License
[MIT](https://choosealicense.com/licenses/mit/)