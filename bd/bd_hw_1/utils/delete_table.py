def delete_table(db_cursor: object, name: str):    
    db_cursor.execute(f"""
        DROP TABLE {name};
    """) 

    return db_cursor