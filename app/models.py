from  . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    '''
    reloads the user from the session
    '''
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__= 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    passecure = db.Column(db.String(255))
    posts = db.relationship('Blog',backref = 'users', lazy = "dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.add(self)
        db.session.commit()

    
    def get_blog(self,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(255),nullable = False)
    content = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.add(self)
        db.session.commit()

    
    def get_blog(self,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'


class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key =True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_commit(self):
        db.session.add(self)
        db.session.commit()

    def get_comment(self,id):
        comment = Comment.query.all(id=id)
        return comment

    def __repr__(self):
        return f'Comment {self.comment}' 


class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'

class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
