from flask import Flask, render_template, request
from luna_obscurify import calculate

app = Flask(__name__)


@app.route('/',  methods=["GET", "POST"])
def run():
    if request.method == 'POST':
        obj_diameter = request.form.get('object-input')
        if obj_diameter == '':
            return render_template("index.html", obj_distance="")
        obj_dist = calculate(obj_diameter=obj_diameter, use_average=False)
        return render_template("index.html", obj_distance=obj_dist)

    if request.method == 'GET':
        return render_template("index.html", obj_distance="")
