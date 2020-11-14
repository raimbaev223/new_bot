import sqlite3


class Data:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    # def create_db(self):
    #     self.connection.execute(
    #         f"CREATE TABLE IF NOT EXISTS images_db(image_id TEXT, name TEXT);"
    #     )
    #     self.connection.commit()

    def add_image(self, image_id, name):
        with self.connection:
            return self.connection.execute(
                f"INSERT INTO 'images_db'"
                f"(`image_id`, 'name') VALUES(?,?)", (image_id, name)
            )

    def get_object(self):
        with self.connection:
            return self.cursor.execute(
                f"SELECT * FROM `images_db`"
            ).fetchall()



dbase = Data('db.db')

