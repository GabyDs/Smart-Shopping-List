import sqlite3
from sqlite3 import Error
from queries import (
    get_query_items,
    get_query_select_name_quantity_from_shooping_id,
    get_query_shopping_list,
    get_query_shopping_list_item,
    get_query_insert_into_shopping_list,
    get_query_insert_into_items,
    get_query_insert_into_shopping_list_items,
)


def create_connection(db_file):
    """create a database connection to the SQLite database specified by db_file

    Args:
        db_file (str): path to database file

    Returns:
        conn (Connection object or None)
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement

    Args:
        conn (Connection object): conecction to database
        create_table_sql (str): sql to create a table
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insertShoppingListRow(conn, shopping_list_data):
    """Create a new row into the shoppingList table

    Args:
        conn (Connection object): conecction to database
        shopping_list_data (tuple): data of the shopping list

    Returns:
        shopping_list_id (int): id of the last added row
    """

    cur = conn.cursor()
    cur.execute(get_query_insert_into_shopping_list(), shopping_list_data)
    conn.commit()
    return cur.lastrowid


def insertIntem(conn, item_data):
    """Create a new item into the items table

    Args:
        conn (Connection object): conecction to database
        item_data (tuple): data of the item

    Returns:
        item_id (int): id of the last added row
    """

    cur = conn.cursor()
    cur.execute(get_query_insert_into_items(), item_data)
    conn.commit()
    return cur.lastrowid


def insertShoppingListItemAssociation(conn, association_data):
    """Link a List with an Item

    Args:
        conn (Connection object): conecction to database
        association_data (tuple): data to link a list with an item
    """

    cur = conn.cursor()
    cur.execute(get_query_insert_into_shopping_list_items(), association_data)
    conn.commit()


def getItemsAndQuantitiesForList(conn, shopping_list_id):
    """Get item names and quantities for a given shopping list

    Args:
        conn (Connection object): conecction to database
        shopping_list_id (int): id of the shopping list

    Returns:
        records (list): List of tuples containing (item_name, quantity)
    """

    cur = conn.cursor()
    cur.execute(get_query_select_name_quantity_from_shooping_id(shopping_list_id))
    records = cur.fetchall()
    return records


def main():

    database = "./src/db/database.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:

        # create tables
        create_table(conn, get_query_shopping_list())
        create_table(conn, get_query_items())
        create_table(conn, get_query_shopping_list_item())

        # Create 3 shopping lists
        shopping_list_1_data = ("Shopping List 1", "2024-02-27", "2024-02-27")
        shopping_list_1_id = insertShoppingListRow(conn, shopping_list_1_data)

        shopping_list_2_data = ("Shopping List 2", "2024-02-27", "2024-02-27")
        shopping_list_2_id = insertShoppingListRow(conn, shopping_list_2_data)

        shopping_list_3_data = ("Shopping List 3", "2024-02-27", "2024-02-27")
        shopping_list_3_id = insertShoppingListRow(conn, shopping_list_3_data)

        # Create 5 items
        item_1_data = ("Bread", "Food")
        item_1_id = insertIntem(conn, item_1_data)

        item_2_data = ("Milk", "Beverage")
        item_2_id = insertIntem(conn, item_2_data)

        item_3_data = ("Meat", "Food")
        item_3_id = insertIntem(conn, item_3_data)

        item_4_data = ("Fruits", "Food")
        item_4_id = insertIntem(conn, item_4_data)

        item_5_data = ("Detergent", "Cleaning")
        item_5_id = insertIntem(conn, item_5_data)

        # Associate some items with the lists
        association_1_data = (shopping_list_1_id, item_1_id, 3)
        insertShoppingListItemAssociation(conn, association_1_data)

        association_2_data = (shopping_list_1_id, item_2_id, 2)
        insertShoppingListItemAssociation(conn, association_2_data)

        association_3_data = (shopping_list_2_id, item_3_id, 1)
        insertShoppingListItemAssociation(conn, association_3_data)

        association_4_data = (shopping_list_2_id, item_4_id, 4)
        insertShoppingListItemAssociation(conn, association_4_data)

        association_5_data = (shopping_list_3_id, item_5_id, 2)
        insertShoppingListItemAssociation(conn, association_5_data)

        # Get Items and Quatities
        records = getItemsAndQuantitiesForList(conn, shopping_list_3_id)
        print(records)

    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
