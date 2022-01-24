"""1. What is a computer program?\n
A.: A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer.\n
2. What's automation?\n
A.: The process of replacing a manual step with one that happens automatically.\n
3. Which of the following tasks are good candidates for automation? Check all that apply.\n
A.: Creating a report of how much each sales person has sold in the last month.\nSetting the home directory and access permissions for new employees joining your company.\nPopulating your company's e-commerce site with the latest products in the catalog.\n
4. What are some characteristics of the Python programming language? Check all that apply.
A.: Python programs are easy to write and understand.\n The Python interpreter reads our code and transforms it into computer instructions.\n We can practice Python using web interpreters or codepads as well as executing it locally.\n
5. How does Python compare to other programming languages?\n
A.: Each programmin language has its advantages and disadvantages.\n"""

# 6. Write a Python script that outputs "Automating with Python is fun!" to the screen.
print('Automating with Python is fun!')

# 7. Fill in the blanks so that the code prints "Yellow is the color of sunshine".
color = 'Yellow'
thing = 'sunshine'
print(color + ' is the color of ' + thing)

"""8. Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week,\n if a week is 7 days. Print the result on the screen.\n
Note: Your result should be in the format of just a number, not a sentence."""
seconds_in_a_day = 86400
seconds_in_a_week = seconds_in_a_day * 7
print(seconds_in_a_week)

"""9. Use Python to calculate how many different passwords can be formed with 6 lower case English letters.\nFor a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.\nUsing this information, print the amount of possible passwords that can be formed with 6 letters."""
letters = 26
passwordlenght = 6
possibilities = letters**passwordlenght
print(possibilities)

"""10. Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB.\nFill in the blank to calculate how many sectors the disk has.\n
Note: Your result should be in the format of just a number, not a sentence."""
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size
print(sector_amount)
