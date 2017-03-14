from . import db 
 
 
class UserProfile(db.Model): 
     userid = db.Column(db.Integer, primary_key=True) 
     username = db.Column(db.String(80), unique=True) 
     first_name = db.Column(db.String(80)) 
     last_name = db.Column(db.String(80)) 
     biography = db.Column(db.String(255)) 
     gender = db.Column(db.String(80)) 
     age = db.Column(db.Integer) 
     photo = db.Column(db.String(80)) 
     profile_created_on = db.Column(db.String(255)) 
     
     
     def __init__(self, userid, username, first_name, last_name,biography, gender, age, photo,profile_created_on):
          
          
          self.userid=userid
          self.username=username
          self.first_name=first_name.title()
          self.last_name=last_name.title()
          self.age=age
          self.biography=biography
          self.gender = gender.upper()
          self.photo=photo
          self.profile_created_on=profile_created_on
 
 
     def is_authenticated(self): 
         return True 
 
 
     def is_active(self): 
         return True 
 
 
     def is_anonymous(self): 
         return False 
 
 
     def get_id(self): 
         try: 
             return unicode(self.id) 
         except NameError: 
             return str(self.id) 
 
 
     def __repr__(self): 
         return '<User %r>' % (self.username) 
