def insert_table(db_cursor: object, for_insert_dict: dict, name: str):    
    keys_string = ""
    values_string = ""


    for k in for_insert_dict["insert_keys"]:
        keys_string = ", ".join(for_insert_dict["insert_keys"])

    for v in for_insert_dict["insert_values"]:
        values_string = ", ".join(for_insert_dict["insert_values"])

    print(values_string)


    db_cursor.execute(f"""
                      INSERT INTO {name}({keys_string}) VALUES({values_string});
                      """) 
    
    db_cursor.connection.commit()

    return db_cursor