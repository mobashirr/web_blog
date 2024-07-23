from app import User, Post,db,app


with app.app_context():
    ''' access the app_context allow to intract with app and get required config'''

    # create users:
    user1 = User.query.filter_by(username="mohamed").first() # query from database
    user2 = User( id=5, username="ahmed2", email='ahmed2@gmail.com', password='pass') # create new record

    # create posts:
    post1 = Post(title="POST 1", content="this is content", author=user1) # note we used author not user_id
    post2 = Post(title="POST 2", content="this is content 2", author=user2) # its expact an instance of type user
    post3 = Post(title="POST 3", content="this is content 2", author=user2)

    # add the users and post to the database:
    db.session.add_all([post1,post2, post3])
    # db.session.add(user2)
    db.session.add_all([user1, user2])

    # save all of this changes to the database:
    # db.session.commit()
    
    # see how the foreign key works:
    for post in user1.posts:
        print(post.title)

    # access the author from post:
    # print(post1.author)

    # delete all tables and records:
    # db.drop_all()
    # create the tables again and the strucure of my models:
    # db.create_all()


    #print(User.query.all())
    #print(Post.query.all())