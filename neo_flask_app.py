from flask import Flask, render_template, request
import neo_stats



app = Flask(__name__)

largest = neo_stats.get_largest_neo()
smallest = neo_stats.get_smallest_neo()
fastest = neo_stats.get_fastest_neo()
largest_delorean = neo_stats.largest_diameter_in_deloreans()
smallest_delorean = neo_stats.smallest_diameter_in_deloreans()
smallest_armadillo = neo_stats.smallest_diameter_in_armadillos()
largest_armadillo = neo_stats.largest_diameter_in_armadillos()
insult = neo_stats.generate_random_insult()
total_phas = neo_stats.get_total_phas()
total_neos = neo_stats.total_neos_today

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

# Function to get the user's chosen NEO

@app.route("/get_asteroid", methods=["POST"])
def get_asteroid():
    stats = {
    "biggest_name" : largest[1],
    "biggest_diameter" : largest[0],
    "fastest_name" : fastest[1],
    "fastest_speed" : fastest[0],
    "smallest_name" : smallest[1],
    "smallest_diameter" : smallest[0],
    "largest_armadillo" : largest_armadillo,
    "smallest_armadillo" : smallest_armadillo,
    "largest_delorean" : largest_delorean,
    "smallest_delorean" : smallest_delorean
    }

    if 'get_asteroid' in request.form.keys():
        asteroid = request.form['get_asteroid']
    
    return render_template('asteroid_return.html', asteroid_form=asteroid, stats=stats) 

# Function to check if the user wants more info on other NEOs

# Function to initiate the greeting

if __name__ == "__main__":
    app.run(debug = True)