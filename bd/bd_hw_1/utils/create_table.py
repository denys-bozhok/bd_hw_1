def create_table(cursor: object, connection: object, titles_dict: dict):    
    string = ''

    name = titles_dict["name"]

    for el in titles_dict:
        string = ", ".join(titles_dict["colums_titles"])

    cursor.execute(f"""
                      CREATE TABLE IF NOT EXISTS {name}({string});
                      """) 
    
    connection.commit()

    return cursor