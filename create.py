from mobash_blog import db,app
from mobash_blog.models import  User, Post


with app.app_context():
    ''' access the app_context allow to intract with app and get required config'''

    # create or query users:
    user2 = User.query.filter_by(username="ahmed2").first() # query from database
    # user2 = User( id=5, username="ahmed2", email='ahmed2@gmail.com', password='pass') # create new record

    # create posts:
    post1 = Post(title="why flask?", content="because flask is easy to play with", author=user2) # note we used author not user_id as variable name
    post2 = Post(title="how to start your busniss?", content="lorem ipsoem ...", author=user2) # its expact an instance of type user
    post3 = Post(title="POST 3", content="this is content 2", author=user2)

    # add the users and post to the database:
    db.session.add_all([post1,post2, post3])
    # db.session.add(user2)
    db.session.add_all([user2])

    # save all of this changes to the database:
    # db.session.commit()
    
    # see how the foreign key works:
    #for post in user1.posts:
    #    print(post.title)

    # access the author from post:
    # print(post1.author)

    # delete all tables and records:
    # db.drop_all()
    # create the tables again and the strucure of my models:
    # db.create_all()


    #print(User.query.all())
    #print(Post.query.all())