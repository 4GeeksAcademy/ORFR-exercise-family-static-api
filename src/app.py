"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    try:
        members = jackson_family.get_all_members()
        # response_body = {
        #     "family": members
        # }
        if members ==[] :
            return jsonify({"error": "no hay miembros"}), 404
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": "error interno de servidor"}), 500


@app.route('/member/<int:id>', methods=['GET'])
def get_one_member(id):
    try:
        members = jackson_family.get_all_members()
        member = jackson_family.get_member(id)
        # response_body = {
        #     "family": members
        # }
        if members ==[] or id >len(members) :
            return jsonify({"error": "no existe el miembro elegido"}), 404   
    
        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": "error interno de servidor"}), 500

@app.route('/member', methods=['POST'])
def new_member():

    body = request.get_json(force=True)
    jackson_family.add_member(body)
    if body is not None:
        return jsonify({"Done": "Se agrego un nuevo miembro"}), 200
    else: 
        return jsonify({"Error": "Error en la creacion de miembro"}), 404
    


@app.route('/member/<int:id>', methods=['DELETE'])
def delete_one_member(id):
        deleted = jackson_family.get_member(id)

        if deleted :
            jackson_family.delete_member(id)
            return jsonify({"done": "miembro "+str(id)+ " eliminado"}), 200  
        else: return jsonify({"error": "no existe el miembro elegido"}), 404
                 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
