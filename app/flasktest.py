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

''' @app.route("/getasteroid", methods=["post"])
def get_asteroid():
    if asteroid_form = request.form.keys():
        asteroid = request.form['asteroid_form']
    else 
        asteroid = none
    return render_template('output.html', asteroid_form=asteroid) '''

@app.route("/getasteroid", methods=["post"])
def get_asteroid():
    asteroid_form = request.form['asteroid_form']
    if asteroid_form.lower() == "fastest":
        asteroid = "{} is the fastest NEO today, racing towards somwhere at a speed of {} kilometers per second.".format(fastest[1], fastest[0])
    elif asteroid_form.lower() == "largest":
        asteroid = "{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(largest[1], largest[0], largest_armadillo, largest_delorean)
    elif asteroid_form.lower() == "smallest":
        asteroid = "{} is the smallest NEO today. It checks in at a paultry {} meters in diameter. \nThat means it's only {} armadillos OR {} Deloreans in diameter!".format(smallest[1], smallest[0], smallest_armadillo, smallest_delorean)
    else: 
        asteroid = None
    return render_template('output.html', asteroid_form=asteroid)    

if __name__ == "__main__":
    app.run(debug=True)