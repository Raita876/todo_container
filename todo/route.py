import responder

from todo.todo import read_todos

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.status_code = 200
    resp.media = {"message": "Hello World!", "status_code": 200}


@api.route("/todos")
def get_todos(req, resp):
    resp_json = read_todos()
    resp.status_code = resp_json.get("status_code", 400)
    resp.media = resp_json


def main():
    api.run(address="0.0.0.0", port=80)
