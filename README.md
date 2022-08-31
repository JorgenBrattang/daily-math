# Daily Math

Daily Math is a Python terminal game which runs on a mock terminal.

The goal is to challange you to complete 5 math questions per day, either go the easy route or the hard one. You will earn treats either way, but at what cost...

Live app: https://daily-math.herokuapp.com/

# User Experiance (UX)
## User Stories
- The game should be easy to navigate
- Should encurage me to complete the daily tasks
- If the question in hand is to hard, give me the solution.

## User feedback
- The game keeps asking if Im sure to procceed, cause I go for the lower age group. I like it easy.. okey.
    - Keeping that feature because it should be a remainder that you need to progress even further and move up to the more challenging questions.

# Development
To Develop this app, the developer had to think how the app would progress throughout it steps which required a bit of thinking and learning how the code flowed. The logic behind all the functions is quite easy if you break them down to smaller chunks, but a bit of thinking is required to make it functional.

# Strategy
The logic behind each function is simple but requires a bit of practice and failure to reach the final product. As mentioned before by breaking down the code into smaller chunks and each function to its core, it is quite easy to code this. But to make it work the developer needs to read documents and tutorials to grasp the concept and the fundamentals.

## Feature / Task list
- Welcome message
- Enter user name
    - Explain that user input i stored in non secured fasion, use fictional enquiry.
    - If first time, create account otherwise move on.
- User login
- Welcome message, maybe qoute of the day.
- Display how many points you need for today.
- Choose diffuculty level.
     - Level 1, preschool
     - Level 2, school
     - Level 3, Real life
           - Score increases per level of       diffuculty.
- Question:
     - Level 1 question, whole text with numbers.
     - Level 2 question, just names and numbers.
     - Level 3 question, equation only.
     - Level 4, still needs help, display part solution.
- Different score for each level, the higher level the lower score.
- Once done, grant a thank you note or similar for completing this weeks homework.
Google sheet tasks:
- Save the user login.
- Keep record of score.
- Level questions.
    - Different score on each level.
- Corresponding equations on the questions for each level.
- Different messages, example "Welcome message".

# Testing
To see the testing part, please follow this link: Testing.md

## Unsolved bugs
- Could not disable the keyboard while the sleep() was working it's magic. Tried different approaces but none that I could implement.

# Technologies used
## Language
- Python

## Frameworks libraries and programs Used
- <a href="https://gitpod.io/" title="Link to gitpod" rel="nofollow">GitPod</a>
    - GitPod was used for writing code, committing, and then pushing to GitHub.
- <a href="https://github.com/" title="Link to github" rel="nofollow">Github</a>
    - GitHub was used to store the project after pushing

## Credit
Quotes of the day:
https://www.brainyquote.com/topics/motivational-quotes

Math questions
- https://www.kidzone.ws/math/wordproblems.htm

- https://www.cuemath.com/learn/fun-maths-questions/#30%20Fun%20Maths%20Questions%20with%20answers

### Credited Code

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

## What I learned
The developer learn basic Python coding and how to implement libarys to make life a little easier, and not invent the wheel again.

## Continued development
To further develop this game, it would be to add even more questions and improve the solution to make a step by step guide to show the user how it was solved.

## Acknowledgements
I would like to acknowledge my mentor <a href="https://github.com/seunkoko" title="Link to GitHub profile" rel="nofollow">Oluwaseun Owonikoko</a> which guided me to make the app more interesting and threw me idea's that I did not think about.

 My family for helping me progress and support me, and not to forget the tutors and community of slack that helped me alot to understand the concepts of programming and hardship of debugging.