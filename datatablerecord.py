import sqlite3
try:
    #Creation of the database to be connected to
    db = sqlite3.connect('record_table_db.db')
    cur = db.cursor()
    cur.execute('Create table record_talbe_item (Chan Saw Juggling Record Holder text, Country text, Number of Cataches int)')
    #Inserting of roleswithin the database
    with db:
        cur.execute('insert into record_talbe_item values("Ian Steward", "Canada", 94)')
        cur.execute('insert into record_talbe_item values("Aaron Gregg", "Canada", 88)')
        cur.execute('insert into record_talbe_item values("Chad Taylor","USA", 78 )')

    with db:
        #printing of various database records
        for row in cur.execute('select * from record_talbe_item'):
            print(row)

        cur.execute("Drop table record_talbe_item")

except sqlite3.Error as e:
    print('Error deleting record tatlbe')

finally:
    #close the database
    db.close()
