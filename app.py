from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import openai_key

openai.api_key = openai_key.API_KEY

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400

    try:

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "system", "content": f"You are an assistant that takes a gist of an email from the user and writes the email (not the reply). Style should be {data['style']}. Lenght should be {data['length']}"},
                   {"role": "user", "content": data['prompt']}
                ]
        )
        print(completion.choices[0].message)
        return jsonify({'response': completion.choices[0].message}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
