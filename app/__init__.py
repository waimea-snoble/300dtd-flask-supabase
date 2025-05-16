from flask import Flask
from flask import render_template
from supabase import create_client
from dotenv import load_dotenv
import os

# Get environemnt variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase as a client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print(supabase)

# Create the Flask app
app = Flask(__name__)


@app.get("/")
def home():
    response = supabase.table("things").select().execute()
    records = response.data

    return render_template("pages/home.jinja", things=records)

@app.errorhandler(404)
def notFound(error):
    return render_template("pages/404.jinja")

