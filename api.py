import flask
from flask import jsonify, request

from fastai.vision import load_learner

from io import BytesIO

app = flask.Flask(__name__)
app.config["DEBUG"] = True

tree_learner = load_learner('export_learners', 'trees.pkl')


@app.route('/trees', methods=['GET'])
def trees():
    if 'img' in request.args:
        img = open_image(BytesIO(request.args['img']))
        prediction = int(tree_learner.predict(img))
        return jsonify(
            {
                'prediction': prediction
            }
        )