from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import CommentsForm, UpdateFrofile, BlogForm,UpvoteForm
from .models import User, Blog, CommentsForm
from flask_login import login_required, current_user
from .. import db

@main('/')
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

@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_blog:
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
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
