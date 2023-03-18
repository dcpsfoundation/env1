# from io import BytesIO
import json
from flask import Flask, render_template, url_for,json,request, send_file,jsonify 
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import secure_filename
import os

app = Flask(__name__,template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_BINDS'] = {'test2':'sqlite:///test2.db','test3':'sqlite:///test3.db','test4':'sqlite:///test4.db'}
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

# Get the list of all files and directories
path = "static/uploadFiles"
dir_list = os.listdir(path)
dir_length = len(dir_list)
def capitMyfiles(self):
        a = self.os.listdir(self.path)
        for i in a:
            t = i.split(".")
            if t[0] != t[0].capitalize():
                self.os.rename(i,t[0].capitalize()+"."+t[1])
msg = ""
# class Upload(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     img = db.Column(db.Text,unique=True,nullable=False)
#     name = db.Column(db.Text, nullable=False)
#     mimetype = db.Column(db.Text, nullable=False)
#     def __repr__(self):
#         return f"id: {self.id}\n filename: {self.img}\n name: {self.name}\n mimetype: {self.mimetype}\n" 
# msg = "" 
class Todo(db.Model):
    user_id = db.Column(db.String(200), nullable=False, unique=True ,primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.Integer,default=0)
 
    def __repr__(self):
        return f"user_id:  -  {self.user_id}  -  full:  -  {self.full_name}  -  state:  -  {self.state} - district:  -  {self.district} - email:  -  {self.email}  -  gender:  -  {self.gender} - date_of_birth:  -  {self.dob}  -  password:  -  {self.password}  -  phone:  -  {self.phone}"
 
 
class Latest(db.Model):
    __bind_key__ = 'test2'
    id = db.Column(db.Integer, unique=True ,primary_key=True)
    img_name = db.Column(db.String(2000), nullable=False)
    title_post = db.Column(db.String(2000), nullable=False)
    descri_post = db.Column(db.String(2000), nullable=False)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"img:  -  {self.img_name}\n  -  title:  -  {self.title_post}\n  -  describtion:  -  {self.descri_post}\n  -  first:  -  {self.first_name}\n  -  last:  -  {self.last_name}\n @#$@#$ "    

class AppForm(db.Model):
    __bind_key__ = 'test3'
    id2 = db.Column(db.Integer, unique=True ,primary_key=True)
    user_id2 = db.Column(db.String(200), nullable=False)
    f_name = db.Column(db.String(200), nullable=False)
    m_name = db.Column(db.String(200), nullable=False)
    l_name = db.Column(db.String(200), nullable=False)
    father_husband = db.Column(db.String(200), nullable=False)
    mother = db.Column(db.String(200), nullable=False)
    email_id = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.String(200), nullable=False)
    alt_phone_no = db.Column(db.String(200), nullable=False)
    aadhar =db.Column(db.String(200), nullable=False)
    dateOB = db.Column(db.String(200), nullable=False)
    gender2 = db.Column(db.String(200), nullable=False)
    marital = db.Column(db.String(200), nullable=False)
    pan_no = db.Column(db.String(200), nullable=False)
    cast = db.Column(db.String(200), nullable=False)
    blood = db.Column(db.String(200), nullable=False)
    qualification = db.Column(db.String(200), nullable=False)
    address1 = db.Column(db.String(200), nullable=False)
    address2 = db.Column(db.String(200), nullable=False)
    state2 = db.Column(db.String(200), nullable=False)
    district2 = db.Column(db.String(200), nullable=False)
    pin = db.Column(db.String(200), nullable=False)
    job = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(200), nullable=False)
    appointment = db.Column(db.String(200), nullable=False)
    appoint_date = db.Column(db.String(200), nullable=False)
    retire_date = db.Column(db.String(200), nullable=False)
    member = db.Column(db.String(200), nullable=False)
    imgName = db.Column(db.String(2000), nullable=False)
    
    def __repr__(self):
        return f"id:  -  {self.id2}  -  user_id:  -  {self.user_id2}  -  first_name:  -  {self.f_name}  -  middle_name:  -  {self.m_name}  -  last_name:  -  {self.l_name}  -  father_or_husband:  -  {self.father_husband}  -  mother_name:  -  {self.mother}  -  email_id:  -  {self.email_id}  -  phone_no:  -  {self.phone_no}  -  alt_phone_no:  -  {self.alt_phone_no}  -  aadhar:  -  {self.aadhar}  -  dateOB:  -  {self.dateOB}  -  gender:  -  {self.gender2}  -  marital:  -  {self.marital}  -  pan_no:  -  {self.pan_no}  -  cast:  -  {self.cast}  -  blood:  -  {self.blood}  -  qualification:  -  {self.qualification}  -  address1:  -  {self.address1}  -  address2:  -  {self.address2}  -  state2:  -  {self.state2}  -  district2:  -  {self.district2}  -  pin:  -  {self.pin}  -  job:  -  {self.job}  -  department:  -  {self.department}  -  appointment:  -  {self.appointment}  -  appoint_date:  -  {self.appoint_date}  -  retire_date:  -  {self.retire_date}  -  member:  -  {self.member}  -  imgName:  -  {self.imgName} - "

class Password(db.Model):
    __bind_key__ = 'test4'
    id3 = db.Column(db.Integer, unique=True ,primary_key=True)
    secrete_id = db.Column(db.String(200), nullable=False)
    secrete_key = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"{self.secrete_id},{self.secrete_key}"
    
    


@app.route("/static/register/<string:info>",methods=['POST'])
def process2(info):
    
    info = json.loads(info)
    data = Todo(user_id=(info['user_id']),full_name=(info['full_name']),state = (info['state']),district = (info['district']),email = (info['email']),gender = (info['gender']),dob = (info['dob']),password = (info['password']),phone = (info['phone']))
    
    db.session.add(data)
    db.session.commit()
    
    msg = str(Todo.query.order_by(Todo.user_id).all()).replace("[","").replace("]","").replace("\n"," ")
    
    return msg
    
@app.route("/home/<string:info>",methods=['POST'])
def process1(info):
    info = json.loads(info)
    data2 = Latest(img_name=(info['img_name']),title_post=(info['title_post']),descri_post = (info['descri_post']),first_name = (info['first_name']),last_name = (info['last_name']))
    db.session.add(data2)
    db.session.commit()
    return f'ved'

@app.route("/home/api/<string:temp>",methods=['POST'])
def messenger(temp):
    
    msg = str(Todo.query.order_by(Todo.user_id).all()).replace("[","").replace("]","").replace("\n"," ")
      
    return msg
    
@app.route("/home",methods=['POST','GET'])
def index():
    dataSet = str(Latest.query.order_by(Latest.id).all()).replace("[","").replace("]","").split(",")
    
    return render_template('index.html', dataSet = dataSet)


@app.route("/api/datasetOfpasswordVed@123")
def geo_code():
    dataSet = str(Latest.query.order_by(Latest.id).all()).replace("[","").replace("]","").replace("\n","").split(",")
    return dataSet

@app.route("/api/StateDistrictOfpasswordVed@123")
def stateDistrict():
    
    return render_template('stateDistrict.json')

@app.route("/static/register",methods=['POST','GET'])
def register():
    
    return render_template('registration.html')

@app.route("/static/application/<string:info>",methods=['POST'])
def process3(info):
    info = json.loads(info)
    # print(info['highScore'])
    data = AppForm(user_id2=(info['user_id2']),f_name=(info['f_name']),m_name=(info['m_name']),l_name=(info['l_name']),father_husband=(info['father_husband']),mother=(info['mother']),email_id=(info['email_id']),phone_no=(info['phone_no']),alt_phone_no = (info['alt_phone_no']),aadhar = (info['aadhar']),dateOB = (info['dateOB']),gender2 = (info['gender2']),marital = (info['marital']),pan_no = (info['pan_no']),cast = (info['cast']),blood = (info['blood']),qualification = (info['qualification']),address1 = (info['address1']),address2 = (info['address2']),state2 = (info['state2']),district2 = (info['district2']),pin = (info['pin']),job = (info['job']),department = (info['department']),appointment = (info['appointment']),appoint_date = (info['appoint_date']),retire_date = (info['retire_date']),member = (info['member']),imgName = (info['imgName']))
    
    db.session.add(data)
    db.session.commit()
        
    return "application form submitted :)"
@app.route("/static/applica/<string:temp>",methods=['POST'])
def process2334(temp):
    msg = str(AppForm.query.order_by(AppForm.user_id2).all()).replace("[","").replace("]","").replace("\n"," ")
    return msg
@app.route("/static/application",methods=['POST','GET'])
def application():
    return render_template('application_form.html')

@app.route("/static/admin@70304939602989adminPageToViewDetailsGfrstn",methods=['POST','GET']) 
def adminPage():
    return render_template('admin.html')

@app.route("/static/admin/<string:temp>",methods=['POST'])
def adminRender(temp):
    msg1 = str(Todo.query.order_by(Todo.user_id).all()).replace("[","").replace("]","")
    msg2 = str(AppForm.query.order_by(AppForm.id2).all()).replace("[","").replace("]","")
    return f'{msg1}@#@#@#@#@#{msg2}'

@app.route("/static/adminPass/<string:temp>",methods=['POST'])
def passRender(temp):
    
    return str(Password.query.order_by(Password.id3).all()).replace("[","").replace("]","")
       
@app.route("/static/forget?",methods=['POST','GET'])
def forget():
    return render_template('forget.html')

if __name__ == "__main__":
    app.debug=True
    app.run()