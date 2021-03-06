<<<<<<< HEAD
from flask import render_template,request,redirect,url_for,abort
<<<<<<< HEAD
from flask_login import login_required,current_user
from flask_login import UserMixin
from ..models import Reviews,User
from .forms import ReviewForm,UpdateProfile
from ..import db,photos

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

        return render_template("profile/update.html", form = form)

@main.route('/hostel/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    hostel = get_hostel(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        #update review instance
        new_review = Review(hostel_id=hostel.id,hostel_title=title,image_path=hostel.poster,hostel_review=review,user=current_user)

        #save review method
        new_review.save_review()
        return redirect(url_for('.hostel',id = hostel.id))

    title = f'{movie.title} review'
    return redirect(url_for('.new_review.html',title = title, review_form=form, movie=movie))
        

=======
from . import main
from ..models import Review
import markdown2
from .forms import ReviewForm
from .. import db,photos
from datetime import datetime
from flask_login import login_required,current_user


@main.route("/<user>/hostel/<hostel_id>/add-review", methods = ["GET","POST"])
@login_required
def review(user,review_id):
    user = User.query.filter_by(id = user).first()
    review = Review.query.filter_by(id = pitch_id).first()
    form = ReviewForm()
    title = "Add review"
    if form.validate_on_submit():
        content = form.comment.data 
        posted = datetime.now()
        new_review = Review(user = user,review = form.review.data,posted = posted)
        new_review.save_comment()
    #     return redirect(url_for("main.view_comments", pitch_id=pitch.id))
    # return render_template("/new_comment.html", title = pitch.title,form = form,pitch = pitch)
>>>>>>> review
=======
from flask import render_template,redirect,url_for,abort,request
from .forms import SearchForm
from ..models import University
from app import create_app
from . import main
from .. import db
from flask import flash

# init_db()
@main.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@main.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = db_session.query(Hostel)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
# display results
    else:
        return render_template('results.html', results=results)



if __name__ == '__main__':
    app.run()
>>>>>>> searchHostel
