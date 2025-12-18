This is a simple automatic clock-in program. The motivation for writing this program was simply that the author is very forgetful and kept forgetting to clock in every day. In a moment of frustration, the author wrote this program.

Please note that this program is intended for use with NTU’s clock-in system only.

1. Please modify the account credentials in card.py and card_out.py:

username_input.send_keys("your_username")
password_input.send_keys("your_password")


2. Please change the program path in the .bat file to your own path.
   Both programs have a .bat file ready—simply run it to execute the program.

3. You can use Windows Task Scheduler to set a specific time for the program to start.

Note: A small random factor is added to the program so that the clock-in time varies slightly each time.

This program is designed for forgetful people, but remember to still be punctual at work.
