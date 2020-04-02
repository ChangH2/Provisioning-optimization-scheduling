from flask import Flask, jsonify
from flask_restful import Resource, Api
from requests import put, get

app = Flask(__name__)
api = Api(app)


@app.route('/api/nodes')
def test():
    node_list = get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/nodes').json().get('items')
    nodes = dict()
    for n in node_list:
        node = dict()
        node["cpu"] = n.get('usage').get('cpu')
        node["memory"] = n.get('usage').get('memory')
        nodes[n.get('metadata').get('name')] = node
    return nodes


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
