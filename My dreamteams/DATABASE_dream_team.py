import psycopg2


# Task 1

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT * FROM kivano WHERE category_id = 1 AND price IN (SELECT price FROM sulpak WHERE category_id = 2 AND kivano.price = price)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 2

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT MIN(sulpak.product_name) FROM sulpak JOIN kivano USING(product_name) WHERE sulpak.product_name LIKE 'Iphone %'")
#
# print(cur.fetchall())
#
# conn.close()
# cur.close()


# Task 3


# Task 4

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT * FROM kivano WHERE produser_id IN (SELECT produser_id FROM produsers WHERE produser_country = 'China')")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 5

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name, price, prodused_date FROM kivano JOIN produsers USING(produser_id) ORDER BY prodused_date")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 6

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name FROM kivano EXCEPT SELECT product_name FROM sulpak")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 7

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name, price FROM sulpak WHERE product_name LIKE '%M%' OR product_name LIKE '%m%'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 8

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name FROM sulpak INTERSECT SELECT product_name FROM kivano")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 9
# SELECT product_name FROM kivano JOIN produsers USING(produser_id) WHERE produser_country = 'China' AND product_name LIKE '%k%'

# Task 10

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute(f"UPDATE produsers SET produser_country = 'Kyrgyzstan', produser_company = 'Mac' WHERE prodused_date = (SELECT MAX(prodused_date) FROM produsers)")
# cur.execute("SELECT * FROM produsers ORDER BY prodused_date")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 11

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT sulpak.product_name, sulpak.price, kivano.product_name, kivano.price FROM sulpak FULL JOIN kivano USING(product_name)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()

# Task 12

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM produsers WHERE prodused_date = (SELECT MAX(prodused_date) FROM produsers WHERE produser_country = 'Japan')")
# print(cur.fetchall())
#
# conn.close()
# cur.close()


# Task 13

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("UPDATE sulpak SET price = price + 1000")
# cur.execute("SELECT product_name, price FROM sulpak")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 14

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT (SELECT MAX(price) FROM kivano) - (SELECT MAX(price) FROM sulpak)")
# print(cur.fetchall())
#
# conn.close()
# cur.close()


# Task 15

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT product_name, price FROM sulpak WHERE price = (SELECT MIN(price) FROM sulpak WHERE category_id = 1) UNION ALL SELECT product_name, price FROM kivano WHERE price = (SELECT MIN(price) FROM kivano WHERE category_id = 1)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 16
# DELETE FROM kivano WHERE product_name = NULL;


# Task 17

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("UPDATE produsers SET prodused_date = '2000-01-01' WHERE prodused_date IN (SELECT prodused_date FROM kivano JOIN produsers USING(produser_id) WHERE prodused_date < '1998-12-31')")
# cur.execute("SELECT product_name, price, prodused_date FROM kivano JOIN produsers USING(produser_id)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 18

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("UPDATE produsers SET produser_country = 'Germany' WHERE produser_country = (SELECT produser_country FROM produsers WHERE produser_country = 'Brazil' AND prodused_date > '2012-01-01' AND produser_company = 'Aser')")
# cur.execute("SELECT * FROM produsers WHERE produser_company = 'Aser' AND prodused_date > '2012-01-01'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 19

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT product_name, price FROM kivano LIMIT 16")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 20

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT product_name FROM kivano WHERE category_id = 2")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 21

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM sulpak WHERE price BETWEEN (SELECT AVG(price) FROM sulpak) - 2000 AND (SELECT AVG(price) FROM sulpak) + 2000")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 22

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT produser_company, price FROM produsers JOIN kivano USING (produser_id) WHERE price > (SELECT AVG(price) FROM kivano)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 23

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM sulpak WHERE item_id = (SELECT COUNT(item_id) FROM sulpak) / 2")
# print(cur.fetchall())
#
# conn.close()
# cur.close()


# Task 24

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("UPDATE produsers SET produser_country = 'South Korea' WHERE produser_id IN (SELECT produser_id FROM produsers WHERE produser_country = 'Korea' AND produser_company = 'Asus')")
# cur.execute("SELECT produser_country, produser_company FROM produsers WHERE produser_company = 'Asus'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Task 25

# conn = psycopg2.connect(dbname='for_dreamteam', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("UPDATE produsers SET produser_company = 'Microsoft' WHERE produser_id IN (SELECT produser_id FROM produsers WHERE produser_company = 'Nokia' AND produser_country = 'USA')")
# cur.execute("SELECT * FROM produsers WHERE produser_company = 'Nokia'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()