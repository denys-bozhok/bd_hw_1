from components.Customer import *
from components.Dish import *
from components.Order import *

from utils.db_utils import create_db, get_data
from utils.create_table import create_table
from utils.delete_table import delete_table
from utils.insert_table import insert_table

from utils.get_class_name import get_class_name
from utils.get_list_for_colum_names import get_list_for_colum_names
from utils.get_insert_dict import get_insert_dict


def main():

    # -----------------INSTANCES-----------------

    customer = Customer("John", "Doe", 500).__dict__

    customers_arr = [Customer("John", "Doe", 500).__dict__,
                     Customer("Misha", "Doets", 700).__dict__,
                     Customer("Sanya", "Dolb", 350).__dict__,
                     Customer("Kirill", "Great", 100000000).__dict__,
                     Customer("Miron", "Duke", 666).__dict__,
                     Customer("Cristoph", "Ramm", 1988).__dict__,
                     Customer("Till", "Lendermahn", 10000).__dict__
                     ]
    
    dish = Dish("pasta", 12).__dict__
    
    orders = Orders(1, 1).__dict__


    # -----------------CREATE_DB-----------------
    # db_name = input("Enter DB name\n")
    
    db_cursor = create_db("hw_db")

    cursor, connection = get_data(db_cursor)


    # -----------------CREATE_TABLE-----------------
    # table_name = get_class_name(Orders)
    # table_dict = get_list_for_colum_names(orders, table_name)

    # create_table(cursor, connection, table_dict)

   # -----------------DELETE_TABLE-----------------
    # table_name = get_class_name(Orders)
    # delete_table(cursor, connection, table_name)


    # ----------------INSERT_INTO_TABLE-----------------
    table_name = get_class_name(Customer)

    for inst in customers_arr:
        
        insert_dict = get_insert_dict(inst)
        insert_table(cursor, connection, insert_dict, table_name)



if __name__ == "__main__":
    main()

