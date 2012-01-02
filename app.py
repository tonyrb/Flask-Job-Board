import os
from datetime import datetime
from flask import Flask, render_template
import settings
from mongoengine import connect, Document, StringField, EmailField, BooleanField, DateTimeField, URLField

app = Flask(__name__)
app.config.from_object(settings)

connect('app2312735', 
        host='staff.mongohq.com',
        port=10092, 
        username='heroku',
        password='ded467f4021d3ca1c394707cbb2a8760')

class User(Document):
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Job(Document):
	company_name = StringField(required=True)
	company_location = StringField(required=True)
	company_url = URLField(required=True)
	job_posting = StringField(required=True)
	application_instructions = StringField(required=True)
	telework = BooleanField(required=True)
	created = DateTimeField(default = datetime.utcnow())

@app.route("/")
def hello():
    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)