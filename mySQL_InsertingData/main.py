import mysql.connector

list = []
while True:
    name = input("Product name: ")
    price = float(input("Product price: "))
    imageUrl = input("Product imageUrl: ")
    description = input("Product description: ")
    list.append((name, price, imageUrl, description))
    resp = input("Are you want to add more product (y/n) ?")
    if resp == 'n' or resp == 'N':
        print(list)
        print("Your list is adding to the database")
        break

for i in list:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*************",
        database="node-app")
    cursor = connection.cursor()
    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = (i[0], i[1], i[2], i[3])
    cursor.execute(sql, values)
    # cursor.executemany(list)

    try:
        connection.commit()
        print(f"{cursor.rowcount} new data added.")
        print(f"Id of last data: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)

    finally:
        connection.close()
        print("Database Connection closed")

# insertProduct(name, price, imageUrl, description)
