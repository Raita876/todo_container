from dataclasses import dataclass
import pymysql
from datetime import datetime
from typing import List
from todo.exceptions import DatabaseError


@dataclass
class Todo:
    id: str
    name: str
    tag: str
    memo: str
    create_date: datetime
    update_date: datetime
    close_date: datetime

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "tag": self.tag,
            "memo": self.memo,
            "create_date": self.create_date.strftime("%Y-%m-%d %H:%M:%S"),
            "update_date": self.update_date.strftime("%Y-%m-%d %H:%M:%S"),
            "close_date": self.close_date.strftime("%Y-%m-%d %H:%M:%S"),
        }


class DatabaseController:
    def __init__(
        self,
        host: str = None,
        user: str = None,
        password: str = None,
        db: str = None,
        charset: str = None,
    ):
        self.host = "database" if host is None else host
        self.user = "example" if user is None else user
        self.password = "example" if password is None else password
        self.db = "todo_app" if db is None else db
        self.charset = "utf8mb4" if charset is None else charset

    def __connect(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                charset=self.charset,
                cursorclass=pymysql.cursors.DictCursor,
            )

        except pymysql.err.MySQLError as e:
            raise DatabaseError("Database connection Error.")

        return connection

    def get_all(self) -> List[Todo]:
        todos = []
        conn = None

        try:
            conn = self.__connect()

            with conn.cursor() as cursor:
                sql = (
                    "SELECT id, name, tag, memo, create_date, update_date, close_date "
                    + "FROM todo "
                    + "ORDER BY create_date ASC"
                )

                cursor.execute(sql)
                results = cursor.fetchall()

                for result in results:
                    todo = Todo(
                        id=result["id"],
                        name=result["name"],
                        tag=result["tag"],
                        memo=result["memo"],
                        create_date=result["create_date"],
                        update_date=result["update_date"],
                        close_date=result["close_date"],
                    )

                    todos.append(todo)

        except pymysql.err.MySQLError as e:
            raise DatabaseError("Database Get Todos Error.")

        finally:
            if conn is not None:
                conn.close()

        return todos


def read_todos() -> dict:
    try:
        ctr = DatabaseController()
        todos = ctr.get_all()
        todos_dict = [todo.to_dict() for todo in todos]

    except pymysql.err.MySQLError as e:
        return {"status_code": 500, "message": e.message}

    except Exception as e:
        return {"status_code": 400, "message": e.message}

    return {"status_code": 200, "items": todos_dict}
