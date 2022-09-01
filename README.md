# Daily Math

Daily Math is a Python terminal game which runs on a mock terminal.

The goal is to challange you to complete 5 math questions per day, either go the easy route or the hard one. You will earn treats either way, but at what cost...

![stretch-page](assets/images/amIresponsive.png)

Live app: https://daily-math.herokuapp.com/

# Table of content
- [User Experience](#user-experience)
    - [User stories](#user-stories)
    - [User feedback](#user-feedback)
- [Design](#design)
    - [Login](#login)
    - [Menu](#menu)
    - [Difficulty](#difficulty)
- [Development](#development)
- [Strategy](#strategy)
- [Feature and Testing](#feature-and-testing)
- [Unsolved bugs](#unsolved-bugs)
- [Technologies used](#technologies-used)
    - [Language](#language)
- [Frameworks libraries and programs used](#frameworks-libraries-and-programs-used)


# User experience
## User stories
- The game should be easy to navigate
- Should encurage me to complete the daily tasks
- If the question in hand is to hard, give me the solution.

## User feedback
- The game keeps asking if Im sure to procceed, cause I go for the lower age group. I like it easy.. okey.
    - Keeping that feature because it should be a remainder that you need to progress even further and move up to the more challenging questions.

# Design
I used <a href="https://lucid.app/">Lucid flowcharts</a> to help me with the flow of the project.

## Login
![stretch-page](assets/images/flowchart/menu_flowchart.png)

## Menu
![stretch-page](assets/images/flowchart/menu_flowchart.png)

## Difficulty
![stretch-page](assets/images/flowchart/difficulty_flowchart.png)


# Development
To Develop this app, the developer had to think how the app would progress throughout it steps which required a bit of thinking and learning how the code flowed. The logic behind all the functions is quite easy if you break them down to smaller chunks, but a bit of thinking is required to make it functional.

# Strategy
The logic behind each function is simple but requires a bit of practice and failure to reach the final product. As mentioned before by breaking down the code into smaller chunks and each function to its core, it is quite easy to code this. But to make it work the developer needs to read documents and tutorials to grasp the concept and the fundamentals.

Everything that is entered, like username, age and so on. Will be stored on a seperate server Google sheet API. Which will be read and changed through out the code.

## Feature and Testing
I have combined these two to make space here, cause feature contains of 40 images. So by combining them will make it easier to follow along instead of contant repetition.

Follow this <a href="https://github.com/JorgenBrattang/daily-math/blob/main/TESTING.md">Testing.md</a> to go there.

## Unsolved bugs
- Could not disable the keyboard inbetween loading times, but I have an idea how to fix it. Sadly don't have enough time to fix it.
    - The Idea is to make a function thats freeze the users input before they are prompted to enter something. And then unfreeze it when they need to enter something.

# Technologies used
## Language
- Python

## Frameworks libraries and programs used

- <a href="https://git-scm.com/" title="Link to git" rel="nofollow">Git</a>
    - For version control
- <a href="https://gitpod.io/" title="Link to gitpod" rel="nofollow">GitPod</a>
    - GitPod was used for writing code, committing, and then pushing to GitHub.
- <a href="https://github.com/" title="Link to github" rel="nofollow">Github</a>
    - GitHub was used to store the project after pushing
- <a href="https://docs.google.com/spreadsheets/u/0/" title="Link to google spreadsheet" rel="nofollow">Google Sheets</a>
    - To store information
- <a href="https://docs.gspread.org/en/latest/" title="Link to Gspread documentation" rel="nofollow">Gspread</a>
    - To store information
- <a href="https://dashboard.heroku.com/" title="Link to Heroku" rel="nofollow">Heroku</a>
    - To deploy project.
- <a href="https://lucid.app/" title="Link to lucid" rel="nofollow">Lucid</a> 
    - To make flowcharts for the project
- <a href="https://docs.python.org/3/library/random.html" title="Link to python random" rel="nofollow">Random libary</a> 
    - To make random questions / quotes
- <a href="https://docs.python.org/3/library/datetime.html" title="Link to python datetime" rel="nofollow">Datetime libary</a> 
    - To display current date
- <a href="https://docs.python.org/3/library/os.html" title="Link to python os" rel="nofollow">Os libary</a> 
    - To clear the screen
- <a href="https://pypi.org/project/readchar/" title="Link to python readchar" rel="nofollow">Readchar libary</a> 
    - To get the user's keyboard presses
- <a href="https://ui.dev/amiresponsive" title="Link to am i responsive" rel="nofollow">am i responsive</a> 
    - Show of the mock terminal

# Credit

## Deployment description
Huge thank you to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> with the excellent description on how the deployment went. 

## Quotes of the day:
https://www.brainyquote.com/topics/motivational-quotes

```
"Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better." 
- Samuel Beckett
```

## Math questions

- https://www.kidzone.ws/math/wordproblems.htm
    - Example:
```
Ben has 4 peaches. Sarah has 3 peaches. How many peaches do they have in all?
```

- https://www.cuemath.com/learn/fun-maths-questions/#30%20Fun%20Maths%20Questions%20with%20answers
    - Example:
```
What is the number of the missing sequence: 16 09 68 88 ?? 98
```

# Credited Code

- https://teamtreehouse.com/community/using-a-clearscreen-in-pycharm
```python
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
```

- https://www.youtube.com/watch?v=SuEk_TBkReQ&t=2s
```python
def create_chunk_list(my_list, chunk_size):
        """ Creates smaller chunks of list """
        for i in range(0, len(my_list), chunk_size):
            yield my_list[i:i + chunk_size]
```

- https://littlelearningcorner.com/2021/11/fun-math-questions-for-kids-k-2.html

## Great Tutorials

- Register Keypresses
https://pypi.org/project/readchar/

# Deployment
To make this project I used the Code Institute's mock terminal for Heroku and their way of linking to Google Sheet API.

## Create Repository
For this I used Github.
1. Go to your profile, and press on "Repositories".
2. Press "New" (Big green button).
3. There I chose to use a template from Code Institute to have everything I needed for this project.
4. Named my project "daily-math".
5. Then clicked on "Create repository".
6. Onces created, I opened the repository and clicked on "Gitpod" to create a new workplace.

## Github Pages
1. Went to my repository "daily-math".
2. Settings tab.
3. Pages.
4. Chose my branch to be main.
5. Hit save and a couple of minutes later it was deployed.

## Forking
1. Login to Github and go to my <a href="https://github.com/JorgenBrattang/daily-math">repository</a>
2. Find the Fork button o the top right corner.
3. Press it.
4. The fork is now in your own repository.

## Clone
- Credit to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> for the magnificent description!

1. Login to Github and go to my <a href="https://github.com/JorgenBrattang/daily-math">repository</a>
2. Above the list of files click the green ‘code’ button.
3. This will bring up a few options as to how you would like to clone. You can 4. select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
4. Open git bash
5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

## Setting up google sheets API
- Credit to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> for the excellent description!

To set up google sheets API you must;

1. Head to https://console.cloud.google.com/ and sign in or create a free google account.
2. From the google cloud platform dashboard click 'Select a new project'. Then select 'New project'.
3. Create a name for your project under 'Project name' then click 'Create'.
4. This should bring up a box with your project in. Underneath click 'SELECT PROJECT'.
5. From the sidebar navigate to 'APIs and services', 'Library'.
6. In the search bar search for google drive.
7. Select 'Google drive API' and click 'ENABLE'.
8. Click the 'CREATE CREDENTIALS' button located to the top right of the page.
9. From the dropdown menu under 'Which API are you using?' select 'Google drive API'.
10. Under 'What data will you be accessing' choose 'Application data'.
11. Under 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions?' select 'No, i'm not using them' and click 'NEXT'.
12. Enter a Service Account Name. You can name it whatever you like. I would suggest naming it the same as what you named your project. Then click 'CREATE AND CONTINUE'.
13. In the 'Role' dropdown menu select 'Basic', 'Editor', then click 'Continue'.
14. The next page can be left blank so just click 'DONE'.
15. Under 'Service Accounts' find the account you just created and click it.
16. Navigate to the 'KEYS' tab and click 'ADD KEY', 'Create new key'. Select 'JSON' and click 'CREATE'.
17. This will download a json file to your machine. This normally downloads into your 'downloads' folder but if you're unsure you can right click the file once it's downloaded and click 'show in folder' to locate it.
18. Next we will have to link the Google Sheets API. To do this navigate back to the library by clicking on the burger icon in the top left hand corner and selecting 'APIs and services', 'Library' from the dropdown menu.
19. In the search bar search for 'Google Sheets' and select 'Google Sheets API' and click 'ENABLE'.
20. Now, using a programme like Gitpod open or create a repository.
21. Drag and drop the json file that you downloaded earlier into your workspace. Rename this file to 'creds.json'.
22. Open the file and copy the email address under 'client_email' without the quotation marks.
23. Open up the google sheet you want to use and click the 'Share' button.
24. Paste in the client email. Make sure 'Editor' is selected, untick 'Notify people' and then click 'Share'.
25. To protect sensitive information be sure to add your creds.json file to your .gitignore file inside your editor.
26. In order to use our google sheets API you need to install two additional dependencies into your project. To do this, inside your python workspace on the first line input 'import gspread' and on the line beneath input 'from google.oauth2.service_account import Credentials'.

27. Underneath the two imports copy and paste this code, inserting the name of your google spreadsheet where it says 'google_sheet_name_here'.

```
SCOPE = [ "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive" ]

CREDS = Credentials.from_service_account_file('creds.json') SCOPED_CREDS = CREDS.with_scopes(SCOPE) GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) SHEET = GSPREAD_CLIENT.open('google_sheet_name_here')
```

28. Your APIs will now be linked to your project.

## Setting up heroku
- Credit to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> for the beautiful description!

To set up heroku you must;

1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip3 freeze > requirements.txt' then save and push the changes.
2. Go to Heroku.com and sign in or create a free account.
3. From the heroku dashboard click the 'Create new app' button.
4. Name the app something unique and choose what region you are in then click 'Create app'.
5. Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
6. If your project does not use a creds.json file then skip this step. Otherwise, in the field for KEY enter the value CREDS in all capitals. In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
7. In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
8. Scroll down to the Buildpacks section and click 'Add buildpack'.
9. Click Python then save changes.
10. Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
11. Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
12. Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
13. From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
14. Enter the repository name as it is in GitHub and click 'search'.
15. Click the 'connect' button next to the repository to link it to heroku.
16. To deploy, scroll down and click the 'Deploy Branch' button.
17. Heroku will notify you that the app was successfully deployed with a button to view the app.
18. If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

# Developer's part

## What I learned
The developer learn basic Python coding and how to implement libarys to make life a little easier, and not invent the wheel again.

## Continued development
To further develop this game, it would be to add even more questions and improve the solution to make a step by step guide to show the user how it was solved.

## Acknowledgements
I would like to acknowledge my mentor <a href="https://github.com/seunkoko" title="Link to GitHub profile" rel="nofollow">Oluwaseun Owonikoko</a> which guided me to make the app more interesting and threw me idea's that I did not think about.

 My family for helping me progress and support me, and not to forget the tutors and community of slack that helped me alot to understand the concepts of programming and hardship of debugging.

 And can't thank <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> enough for the time saver with the informative description for deployment, saved me hours of writing and I'm so thankfull!