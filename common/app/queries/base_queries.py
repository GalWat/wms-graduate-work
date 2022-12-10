from config import postgres_connections_pool


class BaseQueries:
    def execute(self, query, params=None):
        connection = postgres_connections_pool.getconn()

        with connection.cursor() as cursor:
            cursor.execute(query, params)

            column_names = [col[0] for col in cursor.description]
            return [dict(zip(column_names, row)) for row in cursor]
