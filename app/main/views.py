from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import CommentsForm,BlogForm,UpvoteForm
from app.models import User, Post, Comment, Quote
from flask_login import login_required, current_user
from .. import db

@main.route('/')
def index():
    '''
    view root page of the app which returns the homepage of thapp
    '''
    title = 'Welcome to blog post'

    return render_template('index.html', title =title)

@main.route('/search/<blog_name>')
def search(blog_name):
    '''
    View function to display the search result
    '''
    searched_blog = search_blog(blog_name)
    title = f'search results for {blog_name}'

    return render_template('search.html',blogs = searched_blog)

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog(new_blog):
    '''
    Function that creates new pitches
    '''
    form = BlogForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        blog= form.content.data
        category_id = form.category_id.data
        new_blog= Blog(blog = blog)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form= form)

@main.route('/pitch/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(pitch_id =id,comment=form.comment.data,username=current_user.username,votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('new_comment.html',comment_form=form, vote_form= vote_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that returs  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html',comments = comments, id=id)



@main.route('/test/<int:id>')  
def test(id):
    '''
    this is route for basic testing
    '''
    pitch =Pitch.query.filter_by(id=1).first()
    return render_template('test.html',pitch= pitch)


@main.route('/all_blogs')  
def get_all_blogs():
    
    blogs = Blog.query.all()
    
    return render_template('blogs.html', blogs= blogs)
