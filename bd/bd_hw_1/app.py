from components.Customer import *
from components.Dish import *
from components.Order import *

from utils.create_table import create_table
from utils.delete_table import delete_table
from utils.insert_table import insert_table

from utils.get_class_name import get_class_name
from utils.create_db import create_db
from utils.get_list_for_colum_names import get_list_for_colum_names
from utils.get_insert_dict import get_insert_dict


def main():

    # -----------------INSTANCES-----------------

    customer = Customer("John", "Doe", 500).__dict__
    
    dish = Dish("pasta", 12).__dict__
    
    orders = Orders(1, 1).__dict__


    # -----------------CREATE_DB-----------------
    # db_name = input("Enter DB name\n")
    db_cursor = create_db("hw_db")

    # -----------------CREATE_TABLE-----------------
    # table_name = get_class_name(Orders)
    # table_dict = get_list_for_colum_names(orders, table_name)

    # create_table(db_cursor, table_dict)

   # -----------------DELETE_TABLE-----------------
    # table_name = get_class_name(Orders)
    # delete_table(db_cursor, table_name)


    # ----------------INSERT_INTO_TABLE-----------------
    table_name = get_class_name(Orders)
    insert_dict = get_insert_dict(orders)

    insert_table(db_cursor, insert_dict, table_name)



if __name__ == "__main__":
    main()

