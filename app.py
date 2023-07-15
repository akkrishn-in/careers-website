from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary': 100000
  },
  {
    'id':1,
    'title':'Data Scientist',
    'location':'Trivandrum, India',
    'salary': 100000
  },
  {
    'id':1,
    'title':'Front-End Developer',
    'location':'Noida, India',
  },
  {
    'id':1,
    'title':'Back-End Developer',
    'location':'Kochi, India',
    'salary': 120000
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

if __name__ =="__main__":
  app.run(host='0.0.0.0', debug=True)