
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/provision', methods=['POST'])
def provision():
    data = request.get_json()
    bucket_name = data.get('bucketName')

    os.environ['BUCKET_NAME'] = bucket_name

    try:
        result = subprocess.run(
            ["pulumi", "up", "--yes", "--cwd", "./pulumi_provision"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return jsonify({"message": "Provisioning complete!"})
    except subprocess.CalledProcessError as e:
        return jsonify({"message": "Provisioning failed", "error": e.stderr.decode()}), 500

if __name__ == '__main__':
    app.run(port=5000)
