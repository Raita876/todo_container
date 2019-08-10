import responder
from marshmallow import Schema, fields

from todo.todo import read_todos

description = "This is Sample Web Application. (responder + nginx + mysql)"
api = responder.API(
    title="Todo Application",
    version="1.0",
    openapi="3.0.2",
    docs_route="/docs",
    description=description,
)


class TodoSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    tag = fields.Str()
    memo = fields.Str()
    create_date = fields.Str()
    update_date = fields.Str()
    close_date = fields.Str()


@api.schema("Todos")
class TodosSchema(Schema):
    status_code = fields.Integer(required=True)
    items = fields.List(fields.Nested(TodoSchema()))


@api.route("/todos")
def get_todos(req, resp):
    """Get Todo-List endpoint.
    ---
    get:
        description: Get Todo-List
        responses:
            200:
                description: TodoList returned. 
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/Todos'
    """
    resp_json = read_todos()
    resp.status_code = resp_json.get("status_code", 400)

    resp.media = TodosSchema().dump(resp_json)


def run():
    api.run(address="0.0.0.0", port=80)
