birthday = '1-May-12'

# Goal: print date as "5/1/2012"
from datetime import datetime
new_birthday = datetime.strptime(birthday, '%d-%B-%y')
print(new_birthday.strftime('%-m/%-d/%Y'))