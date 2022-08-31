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
To Develop this app, the developer had to think how the app would progress throughout it steps which required a bit of thinking and learning how the code flowed. Once that is was out of the way, the logic behind each function was simple but required a bit of practice and failure to reach the final product.

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

## Unsolved bugs
- Could not disable the keyboard while the sleep() was working it's magic. Tried different approaces but none that I could implement.

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