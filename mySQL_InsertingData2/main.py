import mysql.connector


def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user="root", password="********", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} data added.')
        print(f"Id of the last data : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('Database connection closed.')


def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user="root", password="********", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} data added.')
        print(f"Id of the last data : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('Database connection closed.')


def getProduct():
    connection = mysql.connector.connect(host="localhost", user="root", password="Messimessi", database="node-app")

    cursor = connection.cursor()

    # cursor.execute("Select * From Products")
    cursor.execute("Select name,price From Products Where price>=420 and name LIKE '%a%' order by price DESC")

    # result = cursor.fetchone()
    # print(f"Name: {result[0]},\nPrice: {result[1]}\n")

    result = cursor.fetchall()
    for product in result:
        print(f"Name: {product[0]},\nPrice: {product[1]}\n")


def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="messiBetter", database="node-app")
    cursor = connection.cursor()
    sql = "Select * from products where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f"Id ={result[0]},\nName: {result[1]},\nPrice: {result[2]}\n")


def updateProduct(name, price, id):
    connection = mysql.connector.connect(host="localhost", user="root", password="alealeael", database="node-app")
    cursor = connection.cursor()
    sql = "Update products Set name=%s, price=%s where id=%s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} data affected.')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('Database connection closed.')


def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="***********", database="node-app")
    cursor = connection.cursor()
    sql = "Delete from products where id = %s "
    values = id,
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} data deleted.')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('Database connection closed.')
