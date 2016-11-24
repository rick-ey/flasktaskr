# db_create.py

# from datetime import date

from project import db
# from project.models import Task, User

# create the database and the db table
db.create_all()

# insert data
# db.session.add(User("admin", "ad@min.com", "admin", "admin"))
# db.session.add(Task("Finish this tutorial", date(2016, 12, 2), 10, date(2016, 12, 16), 1, 1))
# db.session.add(Task("Finish Real Python", date(2016, 12, 5), 10, date(2016, 12, 16), 1, 1))

# commit the changes
db.session.commit()
