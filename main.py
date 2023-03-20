from flask import Flask, request
import re
from utils import correct_text
from typing import Dict, List, Tuple

app: Flask = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post_request() -> Dict[str, str]:
    text: str = request.json["text"]
    prepared_text: str = re.sub(' +', ' ', text).strip()
    corrected_text: str
    missed_space_positions: List[int]
    corrected_text, missed_space_positions = correct_text(prepared_text)
    response: Dict[str, str] = {
        "corrected_text": corrected_text,
        "missed_space_positions": missed_space_positions
    }
    return response


if __name__ == '__main__':
    app.run()
