from Hash import custom_hash
from flask import request, Flask
import string
import random

app = Flask(__name__)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


random_guess = generate_random_string(16)
hash_to_check = custom_hash(random_guess)  # The password which is hashed and you must guess


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        hashed_password = hash_to_check
        return hashed_password.hex(), 200
    elif request.method == 'POST':
        input_password = request.form['password']
        expected_hash = hash_to_check
        if custom_hash(input_password) == expected_hash:
            return "", 200  # Here is the flag which will be returned by the server of you
            # guess the password
        else:
            return "Invalid password", 400


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

