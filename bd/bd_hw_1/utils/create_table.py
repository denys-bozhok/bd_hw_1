def create_table(db_cursor: object, titles_dict: dict):    
    string = ''

    name = titles_dict["name"]

    for el in titles_dict:
        string = ", ".join(titles_dict["colums_titles"])

    db_cursor.execute(f"""
                      CREATE TABLE IF NOT EXISTS {name}({string});
                      """) 
    
    return db_cursor