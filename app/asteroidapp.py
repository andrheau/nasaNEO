from flask import render_template, request, Flask
import neo_stats
import random

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
    i = random.randint(1,8)
    user = {'username': 'Moon Person'}
    return render_template('experimentalasteroid.html', title='Doom', user=user, total_neos=neo_stats.total_neos_today, random_insult=neo_stats.generate_random_insult(i), random_insult2=neo_stats.generate_random_insult(i), total_phas=neo_stats.get_total_phas())

@app.route("/asteroid")
def asteroid():
    user = {'username': 'Moon Person'}
    return render_template('asteroid.html', title='Doom', user=user)

@app.route("/experimentalasteroid")
def experiment():
    return render_template('template.html')

@app.route("/getasteroid", methods=["post"])
def download_file(filename):
    return send_from_directory('/home/name/Music/', filename)

def get_asteroid():
    stats = {
    "supahbig" : largest[1],
    "supahbigdiameter" : largest[0],
    "largest_url" : largest[2],
    "fastestname" : fastest[1],
    "fastestspeed" : fastest[0],
    "smallestname" : smallest[1],
    "smallestdiameter" : smallest[0],
    "largestarmadillo" : largest_armadillo,
    "smallestarmadillo" : smallest_armadillo,
    "largestdelorean" : largest_delorean,
    "smallestdelorean" : smallest_delorean,
    "smallest_url" : smallest[2],
    "fastesturl" : fastest [2]
    }

    if 'asteroid_form' in request.form.keys():
        asteroid = request.form['asteroid_form']
    elif 'largest' in request.form.keys():
        asteroid = 'largest'

    return render_template('output.html', asteroid_form=asteroid, stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
