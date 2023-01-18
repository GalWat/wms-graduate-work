from config import postgres_connections_pool

AUTOCOMMIT = 0


class BaseQueries:
    def execute(self, query, params=None):
        connection = postgres_connections_pool.getconn()
        try:
            connection.set_isolation_level(AUTOCOMMIT)

            with connection.cursor() as cursor:
                cursor.execute(query, params)

                if desc := cursor.description:
                    column_names = [col[0] for col in desc]
                    return [dict(zip(column_names, row)) for row in cursor]
                return []
        finally:
            postgres_connections_pool.putconn(connection)
