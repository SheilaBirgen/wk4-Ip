from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import UpdateFrofile,BlogForm
from app.models import User, Blog, Comment
from flask_login import login_required, current_user
from .. import db
from ..email import mail_message
from app.request import get_quote

@main.route('/')
def index():
    '''
    view root page of the app which returns the homepage of thapp
    '''
    quote= get_quote()
    page = request.args.get('page',1,type =int)
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page)
    return render_template('index.html',quote=quote,blogs=blogs)

@main.route('/new_post',methods=['GET','POST'])
@login_required
def new_blog():
    '''
    View function to display the search result
    '''
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        user_id = current_user._get_current_object().id
        content = form.content.data
        blog = Blog(title = title, content = content,user_id=user_id)
        blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html',form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id = id).all()
    blog = Blog.query.get_or_404(id)
    return render_template('blogs.html',blog = blog ,comment= comments)
    
@main.route('/comment/<blog_id>',methods=['GET','POST'])
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment = request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save_comment()
    return redirect(url_for('main.blog',id= blog.id))

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

@main.route('/blog/<blog_id>/delete', methods=['POST'])
@login_required
def del_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(404)
    db.session.delete(blog)
    db.session.commit()

    flash('Blog Deleted Successfully')
    return redirect(url_for('sign_in.html'))

@main.route('/profile',methods=['GET','POST'])
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file= save_pic(form.profile_pic.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Profile Updated Successfully')
        return redirect(url_for('main.profile'))
    elif request.method =='GET':        
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename='photos' + current_user.profile_pic_path)    
    return render_template('profile/profile.html',form=form)

@main.route('/user/<string:username>')
def user_post(username):
    user = User.query.filter_by(username=username).first()
    blogs = Blog.query.filter_by(user = user ).order_by(Blog.posted.desc()).paginate(page = page)
    return render_template('posts.html',blogs=blogs,user=user)

@main.route('/user/<name>/updateprofile',methods=['GET','POST'])
@login_required
def Updateprof(name):
    form = UpdateProf()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form=form)


def save_pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/photos', picture_filename)

    output_size = (80,80)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main.route('/blog/<blog_id>/update',methods=['GET','POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(404)
    form = CreateBlog()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash('Quote Blog Successfully Updated')
        return redirect(url_for('main.index',id=blog_id))
    if request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('new_blog.html',form = form)
