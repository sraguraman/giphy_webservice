from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/search/<search_term>')
def query_giphy(search_term):
    url = 'http://api.giphy.com/v1/gifs/search'
    key = 'vIa6iVvRwwONNxkoXfSvGnyKuGvDgg3d'
    num_requests_allowed = 5
    payload = {'q':search_term, 'api_key': key, 'limit': num_requests_allowed}
    final_response = parse_json_response(requests.get(url, params=payload))
    return json.dumps({'data': final_response})


def parse_json_response(giphy_request):
    response = giphy_request.json()['data']
    if len(response) > 4:
        return [{'gif_id': response['id'], 'url': response['url']}]
    else:
        return []


if __name__ == '__main__':
    app.run(port=8080, debug=True)
