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