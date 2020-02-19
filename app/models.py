from app import db
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
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    passecure = db.Column(db.String(255))
    posts = db.relationship('Blog',backref = 'users', lazy = "dynamic")

def save_comment(self):
    db.session.add(self)
    db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(blog_id=id).all()
        return comments

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f"User ({self.username}', '{self.email}')"

class Post(db.Model):
    '''
    blog class to define Blog Objects
    '''
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
        

    def save_blog(self):
        '''
        Function that saves blogs
        '''
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User('{self.date_posted}')"  

class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
