import math
import sqlite3


# q1
def price_check(products, productPrices, productSold, soldPrice):
    ans = 0
    for product, price in zip(productSold, soldPrice):
        index = products.index(product)
        if price != productPrices[index]:
            ans += 1
    return ans


# q2
def get_employee_by_department(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    query = """
        SELECT d.name, COUNT(e.ID) as sum
        FROM Department d
        left join Employee e
        ON d.ID = e.Dept_ID
        GROUP BY d.ID
        ORDER BY sum DESC, d.Name;
    """
    cur.execute(query)
    result = cur.fetchall()

    conn.close()
    return result


# q3
def sum_digit(num):
    if num == 0:
        return 0
    return (num % 10) + sum_digit(num // 10)


# q4
def max_num(stream, max_val=-math.inf, count=0, max_count=0):
    if stream:
        x = stream.pop(0)
        if x == 0:
            print("(" + max_val + ";" + max_count + ")")
        elif x > max_val:
            max_val = x
            max_count = count = 1
        elif x == max_val:
            count += 1
        max_num(stream, max_val, count, max_count)


assert price_check(['rice', 'sugar', 'wheat', 'cheese'], [16.89, 56.92, 20.89, 345.99],
                   ['rice', 'cheese'], [18.99, 400.89]) == 2

assert price_check(['rice', 'cheese'], [16.89, 345.99],
                   ['rice', 'cheese'], [18.99, 400.89]) == 2

print(sum_digit(2347623))
