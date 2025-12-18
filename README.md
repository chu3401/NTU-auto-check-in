Description


This is a simple automatic clock-in program. The motivation for writing this program was simply that the author is very forgetful and kept forgetting to clock in every day. In a moment of frustration, the author wrote this program.

Please note that this program is intended for use with NTU’s clock-in system only.

1. Please modify the account credentials in `card.py` and `card_out.py`:<br>
   ```bat
   username_input.send_keys("**your_username**")
   password_input.send_keys("**your_password**")
   ```
2. Please change the program path in the .bat file to your own path.
   Both programs have a .bat file ready—simply run it to execute the program.

3. You can use Windows Task Scheduler to set a specific time for the program to start.

Note: A small random factor is added to the program so that the clock-in time varies slightly each time.

This program is designed for forgetful people, but remember to still be punctual at work.

說明
---------------------------------------

這是一個簡單的自動打卡程式，會寫這個程式的原因就單純是作者很健忘，每天都忘記打卡。一個激動下就寫了這個程式。 
請注意，這只能用在台大的打卡上。

1. 請修改`card.py` 與`card_out.py`中的帳號密碼<br>
   ```bat
   username_input.send_keys("**your_username**")
   password_input.send_keys("**your_password**")
   ```
2. 兩個程式都寫好了一個.bat檔，請修改程式路徑。<br>
   在 `CheckIn.bat` & `CheckOut.bat`中找到：

   ```bat
   cd **`your\path`**
   ```
   將 your\path 改成你電腦上存放 card.py 的完整路徑，例如：<br>
   ```bat
   cd C:\Users\Name\Downloads\auto_checkin
   ```
3. 可以搭配windows 任務管理器來設定時間啟動 <br>

註：程式中加入了一點隨機變數，讓每次打卡時間都會有些許不同。<br>
此程式是為了記性不好的人開發的，上班還是要準時喔。
