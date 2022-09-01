# Testing and features combined
I chose to combine these two, so for each step of the app I run tests like wrong key and such things, so otherwise a whole other document like would exist and thats just repition that we don't need here. With that said. 

To return to the README.md press <a href="https://github.com/JorgenBrattang/daily-math" title="Link to daily math" rel="nofollow">Here</a>

Live app: https://daily-math.herokuapp.com/

# Table of content
- [Validator](#validator)
- [Features and Testing](#features-and-testing)
- [Bugs](#bugs)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)

# Validator
Tested my code with <a href="http://pep8online.com/" title="Link to pep8online" rel="nofollow">PEP8</a> which showed these messages. I saw no purpose to fix those now, cause they are just recommendations.

![stretch-page](assets/images/testing/pep8.png)

[Back to top](#table-of-content)


# Features and Testing
- Welcomes the player to the game and prompts you to answer the question if your a new or old player.

![stretch-page](assets/images/features/1_Welcome.png)

[Back to top](#table-of-content)

- Here we took the route (Y) for yes we are a new user. And here we are prompted to enter our name. Which accepts alphabetic and numeric characters.

![stretch-page](assets/images/features/2_newuser.png)

[Back to top](#table-of-content)

- Tried to enter (!) which is not alphabetic or numeric character, to return we simply press any key. Which sends us back to the previous page.

![stretch-page](assets/images/features/3_alphanumeric.png)

[Back to top](#table-of-content)

- Back at when we were prompted to enter our name I entered more then 15 characters, which is the limit. And again it gives us the path back to previous page.

![stretch-page](assets/images/features/4_to_menu_characters.png)

[Back to top](#table-of-content)

- Now I tried to enter my name "Jörgen" which I already created beforehand, to get this error. Again, we get the path back to previous page.

![stretch-page](assets/images/features/5_already_exists.png)

[Back to top](#table-of-content)

- Now I entered "Brattäng" instead, and that went through. So now I'm prompt to enter a pin code.

![stretch-page](assets/images/features/6_enter_pinCode.png)

[Back to top](#table-of-content)

- I tested to write just "1" and you get an error, this will happen until you enter a 4 digit pin code. No matter what you enter, so it only checks for example: 1234 which I entered.

![stretch-page](assets/images/features/7_pin_not_valid.png)

[Back to top](#table-of-content)

- Here we get prompt to enter our year of birth, and it will give out the same error as before. But with a difference.

![stretch-page](assets/images/features/8_year_of_birth.png)

[Back to top](#table-of-content)

- And as you might have guess, this is the key difference "year of birth". I have chosen not to display that you need to enter a specific year, cause this app will live on forever and I don't want to destroy it for future users.

![stretch-page](assets/images/features/9_year_not_valid.png)

[Back to top](#table-of-content)

- I now entered "1991" which is when I was born, which led us to this page. That tells us the account is setup and ready to start using. And prompts us back to enter name, but with a difference. Now we have entered if we went the route of (N), so we are now a user that already got an account.

![stretch-page](assets/images/features/10_account_setup.png)

[Back to top](#table-of-content)

- Lets see what happens if we write "random". We get told that the account don't exist and get promted to try again. Lets press (N)

![stretch-page](assets/images/features/11_random_entry.png)

[Back to top](#table-of-content)

- We get sent back to the start page. And to get back were we where we just press (N) for new user. And this gives the same errors as before if you enter not alphabetic or numeric, likewise with to many characters. Lets enter "Brattäng" now.

![stretch-page](assets/images/features/1_Welcome.png)

[Back to top](#table-of-content)

- Now we are back to enter our pin code, and the same errors before if you try something else that isn't ours. But a key difference.

![stretch-page](assets/images/features/6_enter_pinCode.png)

[Back to top](#table-of-content)

- I entered not "1234" but "5648" instead and get this, and this will continue until you get it right or fail three times. Lets see what happens after three times.

![stretch-page](assets/images/features/12_wrong_pin.png)

[Back to top](#table-of-content)

- Second try

![stretch-page](assets/images/features/13_wrong_pin.png)

[Back to top](#table-of-content)

- Now we get that we tried 3 times, and get asked if we are "Brattäng" which we entered. And to try again, we will say (Y) to continue, otherwise we will just go back to start screen.

![stretch-page](assets/images/features/14_are_you_name.png)

[Back to top](#table-of-content)

- Now we are finaly logged in, and gets greeted with our name and gets the current date. And to continue on our adventure.

![stretch-page](assets/images/features/15_login_welcome.png)

[Back to top](#table-of-content)

- And we get an inspiring quote that is motivational. This is random, so it's different each time. And again press to continue.

![stretch-page](assets/images/features/16_random_quote.png)

[Back to top](#table-of-content)

- And now we get our goal of our adventure, to gain 5 treats each day. And it tells us our total amount that we accumulate over time. For now these are empty.

![stretch-page](assets/images/features/17_treats_earned.png)

[Back to top](#table-of-content)

- Now we are finally at the menu, where we get choices to make. Lets press (5) to start!

![stretch-page](assets/images/features/18_menu.png)

[Back to top](#table-of-content)

- As suspected we made the wrong choice and gets greeted by an error, lets press any key to continue. And press (1) instead.

![stretch-page](assets/images/features/19_menu_wrong.png)

[Back to top](#table-of-content)

- Now we have a though choice, as we entered year of birth 1991 our age is now "31" at the time of writing this. But first lets check if you press (5) or any other then 1 - 4.

![stretch-page](assets/images/features/20_difficulty_menu.png)

[Back to top](#table-of-content)

- As suspected we get an error message, that we didn't enter the right number. Lets try again with age 3-5 to see what happens.

![stretch-page](assets/images/features/21_difficulty_menu_wrong.png)

[Back to top](#table-of-content)

- Because of my age "31" I get asked if I want to continue on this difficulty cause it was for age 3-5, and same goes for age 6-12 (no difference). So if we press (N) we get thrown back to the difficulty menu. So lets press (Y).

![stretch-page](assets/images/features/22_difficulty_menu_age.png)

[Back to top](#table-of-content)

- First we get asked if we want to go back, and to do that just leave the input field empty and press "Enter". Lets try to answer wrong first.

![stretch-page](assets/images/features/23_age3-5.png)

- We are now told that we got the wrong answer, and got three tries and a choice to be made after that. Lets continue.

![stretch-page](assets/images/features/24_wrong_1.png)

[Back to top](#table-of-content)

- We get thrown back to the question, but without the return. Cause we already know that. Lets continue to answer wrong.

![stretch-page](assets/images/features/25_continue_question.png)

[Back to top](#table-of-content)

- As suspected 2 out of 3. Lets do that again.

![stretch-page](assets/images/features/26_wrong_1.png)

[Back to top](#table-of-content)

- Now we get our choice that was promised. And lets try to press wrong again.

![stretch-page](assets/images/features/27_choice.png)

[Back to top](#table-of-content)

- We get an error, and to continue to try.

![stretch-page](assets/images/features/28_choice_error.png)

[Back to top](#table-of-content)

- If we press (2), we get thrown back to the same question as befor but with three new tries. If we press (3), we go back to the main menu. So lets press (1).

![stretch-page](assets/images/features/28_choice_error.png)

[Back to top](#table-of-content)

- As you can tell I got another question here, due to the fact when I'm doing this I have redo my steps sometimes and since it's random it gave me another question. But the principle is the same, the question is told again and you are given the answer. If we answer (N) we will go back to main menu. So lets press (K) or any other button then (Y) to test it.

![stretch-page](assets/images/features/29_choice_solution.png)

[Back to top](#table-of-content)

- Now we get a suspected error, lets continue.

![stretch-page](assets/images/features/30_solution_error.png)

[Back to top](#table-of-content)

- Lets press (Y) on this to try again.

![stretch-page](assets/images/features/31_solution_error_part2.png)

[Back to top](#table-of-content)

- Now we are back at another random question. Lets answer right, which is (10).

![stretch-page](assets/images/features/32_question_again.png)

[Back to top](#table-of-content)

- First we get greeted that we are correct, and gets a treat for our accomplishment. And displays our todays effort and total. And as you can see that is 3 out of 5 now, and I played two times before this to show one other then 1 out of 5. Lets make it so we get 5 out of 5 to see what happens.

![stretch-page](assets/images/features/33_correct.png)

[Back to top](#table-of-content)

- We get a great job, and we are free to continue. That 5 out of 5 counter will continue to count. So 6 out of 5... and so on. Now we get promted to press (Y) or (N) again. And if we press other that that the previous error we had when we tested solutions error, this will give the same so no need to show that. So lets press (Y) so I can show you another error message which is for the more advance questions, but still avaliable in the lower ages.

![stretch-page](assets/images/features/34_correct_finish.png)

[Back to top](#table-of-content)

- You answer includes a dot, use commas. This is done so no commas is entered when answering the harder questions on the higher age groups. I have chosen not to fix from dot to commas cause most calculations is done using commas. After that we get the 1 out of 3 error message.

![stretch-page](assets/images/features/35_question_error.png)

[Back to top](#table-of-content)

- So lets head back to the main menu.

![stretch-page](assets/images/features/24_wrong_1.png)

[Back to top](#table-of-content)

- So lets head back to the main menu. And press (2).

![stretch-page](assets/images/features/18_menu.png)

[Back to top](#table-of-content)

- And espected a nice motivational quote. Lets continue. And press (3) in the main menu to check my treats.

![stretch-page](assets/images/features/36_another_random_quote.png)

[Back to top](#table-of-content)

- Here we get show that we are complete with our tasks, and as you can see I cheated a little bit, now it shows 8 out of 5 and total earned 14. Just to show you that it will change over time. The total will never get reset, but the 5 out of 5 will get reset when the date is not the same as before. Now all its left to press is 4. Quit.

![stretch-page](assets/images/features/37_my_treats.png)

[Back to top](#table-of-content)

- And we get prompt to anser yes or no.

![stretch-page](assets/images/features/38_quit.png)

[Back to top](#table-of-content)

- If we missclick this happens. So if we press (N) we simply go back to main menu. Lets press (Y).

![stretch-page](assets/images/features/39_quit_error.png)

[Back to top](#table-of-content)

- And you successfully quit the app.

![stretch-page](assets/images/features/40_final_screen.png)

[Back to top](#table-of-content)

# Bugs

## Solved bugs
I had quite a few of bugs when programming, but here are the most annoying.

- Getting the (Y) or (N) question to work properly with the input, I kept getting error when I used the approach to let the user enter by typing. So after a few hours of trying I accepted that I needed another approach which was to collect the key pressed instead. And that worked much better and was easier to catch if the the user miss typed.

- Getting the data from the worksheet, but at a specific random place. This took a while to figure out, but was easy fix when it was to get it working. Simply by erasing the empty rows in the Google Sheet, and my code worked like a charm.

- To center my text, this took a few hours to much to overcome. It kept moving my text to much on each side, so I made a calculationo to fix it. But was told that I used the function center() that's built in to center text. So after reading the documentation more a simple number was just needed and that fixed the problem.

[Back to top](#table-of-content)

## Unsolved bugs
- Could not disable the keyboard inbetween loading times, but I have an idea how to fix it. Sadly don't have enough time to fix it.
    - The Idea is to make a function thats freeze the users input before they are prompted to enter something. And then unfreeze it when they need to enter something.

[Back to top](#table-of-content)