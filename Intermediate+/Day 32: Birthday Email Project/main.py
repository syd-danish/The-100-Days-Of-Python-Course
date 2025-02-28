##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

MY_GMAIL="yasindanish13@gmail.com"
people_data=pd.read_csv('./birthdays.csv')
letter_templates = [open(f"./letter_templates/letter_{i}.txt").read() for i in range(1, 4)]
birthday_dates = {f"{row['year']}-{row['month']}-{row['day']}":f"{row['name']}" for index, row in people_data.iterrows()}
email_addresses={f"{row['name']}":f"{row['email']}" for i,row in people_data.iterrows()}
print(email_addresses)
today=str(dt.date.today())
for i in birthday_dates:
    if i==today:
        selected_letter = random.choice(letter_templates)
        selected_letter = selected_letter.replace('[NAME]', birthday_dates[i])
        name=birthday_dates[i]
        TO_ADDR=email_addresses[name]
        with smtplib.SMTP('smtp.gmail.com', 587) as mail:
            mail.starttls()
            mail.login(user=MY_GMAIL, password='nbik qzck wnqm mdhg')
            mail.sendmail(from_addr=MY_GMAIL,to_addrs=TO_ADDR,msg=f"Subject: Happy Birthday!\n\n {selected_letter}")
