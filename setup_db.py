from mobash_blog import db, app

with app.app_context():
    '''to intial all the tables of my models'''
    db.create_all()
