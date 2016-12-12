
import sqlite3
from phone_modules.call import call


sqlite_file = 'betadatabase.db'    # name of the sqlite database file
table_name = 'EVENTS'	# name of the table to be queried


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
#
# Get all events that need to be triggered.
c.execute('SELECT * FROM {tn} WHERE  lastsentdate < (julianday(date("now"))- julianday(frequency))'.\
        format(tn=table_name))
all_rows = c.fetchall()

for row in all_rows:
        print row
        call(row[2])

c.execute('UPDATE {tn} set lastsentdate = date("now")'. \
          format(tn=table_name))
print('1):', all_rows)

# Closing the connection to the database file
conn.close()
