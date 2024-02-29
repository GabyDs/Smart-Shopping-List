def get_query_shopping_list():
    return """ CREATE TABLE IF NOT EXISTS ShoppingLists (
                    ShoppingListID integer PRIMARY KEY,
                    Name text NOT NULL,
                    CreationDate text,
                    ModificationDate text); """


def get_query_items():
    return """ CREATE TABLE IF NOT EXISTS Items (
                    ItemID integer PRIMARY KEY,
                    Name text NOT NULL,
                    Category text NOT NULL); """


def get_query_shopping_list_item():
    return """ CREATE TABLE IF NOT EXISTS ShoppingListItems (
                    ShoppingListID integer NOT NULL,
                    ItemID integer NOT NULL,
                    Quantity integer NOT NULL,
                    FOREIGN KEY (ShoppingListID) REFERENCES ShoppingLists (ShoppingListID)
                    FOREIGN KEY (ItemID) REFERENCES Items (ItemID)); """


def get_query_insert_into_shopping_list():
    return """ INSERT INTO ShoppingLists(Name,CreationDate,ModificationDate)
               VALUES(?,?,?) """


def get_query_insert_into_items():
    return """ INSERT INTO Items(Name,Category)
               VALUES(?,?) """


def get_query_insert_into_shopping_list_items():
    return """ INSERT INTO ShoppingListItems(ShoppingListID, ItemID, Quantity)
               VALUES(?,?,?) """


def get_query_select_name_quantity_from_shooping_id(shopping_list_id):
    return f""" SELECT Items.Name, ShoppingListItems.Quantity
                FROM Items
                INNER JOIN ShoppingListItems
                ON ShoppingListItems.ItemID = Items.ItemID
                WHERE ShoppingListItems.ShoppingListID = {shopping_list_id}; """


if __name__ == "__main__":
    pass
