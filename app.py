from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_cors import CORS


engine = create_engine("")


Base = automap_base()

Base.prepare(autoload_with=engine)




app = Flask(__name__, template_folder="")

CORS(app)


#################################################
# Flask Routes
#################################################

@app.route("/help")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "/api/player/<player_name><br/>"
        "/api/bypts/<pts><br/>"
        "/api/allplayers<br/>"
    )

@app.route("/")
def index():
    """Render the home page"""
    return render_template('template.html')

@app.route("/api/player/<player_name>")
def by_player(player_name):
    """ search by player """
    session = Session(engine)

    # Query all player
    query_results = session.query(Players).filter(Players.Player == player_name)
    results = [{"id": x.id, "player": x.Player} for x in query_results]

    print(results)
    session.close()
    return jsonify(results)


@app.route("/api/bypts/<pts>")
def by_pts(pts):
    """ search by pts"""
    session = Session(engine)
    # THIS CODE ISN'T FINISHED
    # POINTS ARE TEXT! NOT INTEGERS
    # Query all passengers
    query_results = session.query(Players).filter(Players.PTS > pts)
    results = [{"id": x.id, "player": x.Player, "pts": x.PTS} for x in query_results]

    print(results)
    session.close()
    return jsonify(results)


@app.route("/api/allplayers")
def allplayers():
    """ list of all players as dictionaries """
    session = Session(engine)
    # get all columns
    results = [x.__dict__ for x in session.query(Players)]
    for result in results:
        del result['_sa_instance_state']
    session.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
