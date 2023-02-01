**Language - EN-US**

# Automated testing with Python
## Using Pytest and Selenium

x = "Hello, World!"
print(x)

y = "Hello World!"
print(y)

z = "Hello World!"
print(z)

## $ py hello.py

###### Jokes aside... lol...

Hi, my name is Diego, and although I always wanted to enter the IT world, only now after my 35th birthday did I have the courage to change areas and enter the IT market.
With a lot of effort I got an opportunity in QA, where I started to envision some ideas. I've been studying the Python language for some time now, and I've finally managed to sketch something that bridges the two worlds.

This is a first project that I leave here on Github as public in order to evolve the process of automating functional tests.

-------------------------------------------------- -------------------------------------------------- -----------------

## Automated test framework using Python with HTML report

## Clone this repository: git@github.com:dgarciasaltori/TestAuto.git

This project is part of an initial test automation study using python/pytest with the help of the Selenium framework to perform functional tests on web applications.

If you are interested in leaving comments, feedbacks or criticisms, I will always be available for conversation.
If you want to fork this project to contribute to its growth, let's go together!

The purpose is to improve and enhance knowledge.

###### Requirements can be found: https://pypi.org/

###### Selenium and Pytest are the main ones

-------------------------------------------------- -------------------------------------------------- -----------------

*It is necessary to add some actions within the code for it to work.*
Starting the test:
It can be using the IDE or through the command prompt.

In the IDE of your choice, open the repository and through the terminal: just type in the terminal the command found on line 3 of the file "comentario.py".

In your operating system's CMD or Terminal, access the repository directory:
"Ex: cd /usuário/source/repo" just type in the terminal the command found on line 3 of the file "comentario.py".

## Video: https://youtu.be/OXMU8aqI27E

-------------------------------------------------- -------------------------------------------------- -----------------

## Future Updates...

Next step will be to use BDD (Gherkin) to facilitate writing according to business rules
Possibly Cucumber will be used together with Behave in order to continue using Python as a language.

-------------------------------------------------- -------------------------------------------------- -----------------
## Extras:

@Execute the command: pytest --html=report.html LoginComment.py
The html file will be automatically generated in the root folder containing the test report

@Creating video log -
Run your tests using the command "pytest --video-recording-options=fps=15,codec=vp9 <test_name.py>

@Webdriver can be used: webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge() or webdriver.Chromium()

@Using pytestmark

@pytest.mark.browser
def test_example(browser):
     browser.get("https://www.example.com")
     assert "Example" in browser.title
#Use the command: pytest --browser=chrome test_example.py

@To create comments inside the pytest log
#pytest.logger.info("Filling in the comment field")
Just write whenever you want to get a specific log