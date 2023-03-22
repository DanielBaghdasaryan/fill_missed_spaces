from flask import Flask, request, jsonify
import re
from utils import correct_text
from typing import Dict, List, Tuple, Any

app: Flask = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post_request() -> Tuple[Dict[str, Any], int]:
    data: Dict[str, str] = request.json

    if 'text' not in data:
        return jsonify({'error': '`text` field is required'}), 400
    if len(data['text']) > 512:
        return jsonify({'error': f'Text length should not be longer than 512, given {len(data["text"])}'}), 400

    text: str = request.json["text"]

    # Remove more than one spaces and trim the text
    prepared_text: str = re.sub(' +', ' ', text).strip()

    corrected_text: str
    missed_space_positions: List[int]
    corrected_text, missed_space_positions = correct_text(prepared_text)

    response: Dict[str, str] = {
        "corrected_text": corrected_text,
        "missed_space_positions": missed_space_positions
    }

    return jsonify(response), 200


@app.route('/healthcheck')
def healthcheck() -> Tuple[Dict[str, Any], int]:
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    app.run()
