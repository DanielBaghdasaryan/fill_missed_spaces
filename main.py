from flask import Flask, request
from utils import correct_text
from typing import Dict

app: Flask = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post_request() -> Dict[str, str]:
    text: str = request.json["text"]
    corrected_text: str = correct_text(text)
    response: Dict[str, str] = {
        "corrected_text": corrected_text
    }
    return response


if __name__ == '__main__':
    app.run()
