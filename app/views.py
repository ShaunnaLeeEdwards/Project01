import os, random, datetime 
from app import app, db 
from flask import render_template, request, redirect, url_for, flash, jsonify, make_response 
from forms import SignUpForm 
from models import UserProfile 
from werkzeug.utils import secure_filename 
from datetime import date, datetime
from time import strftime

@app.route('/') 
def home(): 
    return render_template('home.html') 
      
@app.route('/profile', methods=["GET", "POST"]) 
def profile(): 
    form = SignUpForm() 
    
    if request.method == "POST" and form.validate_on_submit():
        
        
        # file_folder = app.config['UPLOAD_FOLDER'] 
         
              
        # Retrieving the User's data from the form
        first_name = form.first_name.data 
        last_name = form.last_name.data 
        age = form.age.data 
        gender = form.gender.data 
        biography = form.biography.data 
          
        #Retrieving and Saving User's photo
        photo = request.files['photo'] 
        photo = secure_filename(photo.filename) 
        photo.save(os.path.join("app/static/uploads", photo)) 
      
        #Randomly generating the User Identification Number, Username and the date the profile was created 
        userid = random.randint(630000000, 700000000)
        username = first_name + str(random.randint(10,100)) 
        profile_created_on = datetime.now().strftime("%a, %d %b %Y")
          
        new_user = UserProfile(userid, username, first_name, last_name, biography, gender, age, photo, profile_created_on) 
              
        db.session.add(new_user) 
        db.session.commit() 
      
        flash("Your profile was successfully created!", 'success') 
        return redirect(url_for('login')) 
    flash_er(form)          
    return render_template('signup.html', form=form) 
 
def flash_er(form):
    for field, errors in form.errors.items():
        
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'danger') 
            
            
@app.route('/profiles', methods=["GET", "POST"]) 
def profiles(): 
    
    users = db.session.query(UserProfile).all() 
    for user in users:
            
        if request.method == "GET": 
            
            user_list = [{"user": user.username, "userid": user.userid}] 
            return render_template("Profiles.html", users=users) 
          
        elif request.method == "POST": 
            response = make_response(jsonify({"users": user_list}))                                            
            response.headers['Content-Type'] = 'application/json'             
            return response 
    return render_template('Profiles.html', users=users) 

@app.route('/profile/<userid>', methods=["GET", "POST"])
def get_profile(userid):
    user = UserProfile.query.filter_by(userid=userid).first()
    photo = url_for('static', filename='uploads/' +user.photo)
    if request.method == "POST":
        return jsonify(userid=user.userid, 
            username=user.username, 
            age=user.age, 
            gender=user.gender, 
            profile_created_on=user.profile_created_on,
            photo=user.photo
            )
            
    else:
        users = {'id':user.userid, 'username':user.username, 'photo':photo, 'age':user.age, 'first_name':user.first_name, 'last_name':user.last_name, 'gender':user.gender, 'biography':user.biography, 'profile_created_on':user.profile_created_on}
        return render_template('MyProfile.html', user=user, users=users)
                 
                 

if __name__ == '__main__': 
    app.run(debug=True,host="0.0.0.0",port="8080") 
