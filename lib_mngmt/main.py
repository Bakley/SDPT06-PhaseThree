from database import db

def soft_delete_decorator(func):
    def wrapper(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        self.updated(deleted=True)
        return res
    return wrapper

class BaseModel:
    table_name = ""
    columns = {}

    @classmethod
    def create_table(cls):
        # import pdb; pdb.set_trace()
        columns_definition = ", ".join([f'{col} {typ}' for col, typ in cls.columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} (id INTEGER PRIMARY KEY, {columns_definition}, deleted BOOLEAN DEFAULT 0)"
        db.execute(query)

    @classmethod
    def all(cls):
        query = f'SELECT * FROM {cls.table_name} WHERE deleted = 0'
        db.execute(query)
        return db.fetchall()
    
    @classmethod
    def get(cls, id):
        query = f'SELECT * FROM {cls.table_name} WHERE id = ? AND deleted = 0'
        db.execute(query)
        return db.fetchone()
    
    def filter(cls, **kwargs):
        conditions = " AND ".join([f'{k} = ?' for k in kwargs.keys()])
        query = f'SELECT * FROM {cls.table_name} WHERE {conditions} AND deleted = 0'
        db.execute(query, tuple(kwargs.values()))
        return db.fetchall()
    
    def save(self):
        # import pdb; pdb.set_trace()
        columns = ', '.join(self.columns.keys())
        placeholder = ', '.join(["?" for _ in self.columns])
        values = tuple(getattr(self, col) for col in self.columns.keys())
        query = f'INSERT INTO {self.table_name} ({columns}) VALUES ({placeholder})'
        db.execute(query, values)
        self.id = db.cursor.lastrowid

    def update(self, **kwargs):
        set_clause = ', '.join([f'{k} = ?' for k in kwargs.keys()])
        values = tuple(kwargs.values())
        query = f'UPDATE {self.table_name} SET {set_clause} WHERE id = ?'
        db.execute(query, values + (self.id,))

    @classmethod
    @soft_delete_decorator
    def delete(cls, id):
        query = f'UPDATE {cls.table_name} SET deleted = 1 WHERE id = ?'
        db.execute(query, (id,))
        