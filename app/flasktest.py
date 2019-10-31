from flask import render_template, request, Flask
import neo_stats

app = Flask(__name__)

largest = neo_stats.get_largest_neo()
smallest = neo_stats.get_smallest_neo()
fastest = neo_stats.get_fastest_neo()
largest_delorean = neo_stats.largest_diameter_in_deloreans()
smallest_delorean = neo_stats.smallest_diameter_in_deloreans()
smallest_armadillo = neo_stats.smallest_diameter_in_armadillos()
largest_armadillo = neo_stats.largest_diameter_in_armadillos()


@app.route("/")
def home():
    user = {'username': 'Moon Person'}
    return render_template('template.html', title='Doom', user=user)

@app.route("/asteroid")
def asteroid():
    user = {'username': 'Moon Person'}
    return render_template('asteroid.html', title='Doom', user=user)

@app.route("/experimentalasteroid")
def experiment():
    return render_template('experimentalasteroid.html')

@app.route("/getasteroid", methods=["post"])
def get_asteroid():
    stats = {
    "supahbig" : largest[1],
    "supahbigdiameter" : largest[0],
    "fastestname" : fastest[1],
    "fastestspeed" : fastest[0],
    "smallestname" : smallest[1],
    "smallestdiameter" : smallest[0],
    "largestarmadillo" : largest_armadillo,
    "smallestarmadillo" : smallest_armadillo,
    "largestdelorean" : largest_delorean,
    "smallestdelorean" : smallest_delorean
    }

    if 'asteroid_form' in request.form.keys():
        asteroid = request.form['asteroid_form']
    
    return render_template('output.html', asteroid_form=asteroid, stats=stats)    

if __name__ == "__main__":
    app.run(debug=True)

