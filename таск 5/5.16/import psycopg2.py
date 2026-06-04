import psycopg2

# Данные для подключения (из ваших предыдущих шагов в DBeaver)
db_params = {
    "host": "127.0.0.1",
    "port": "5440",
    "database": "testdb",
    "user": "admin",
    "password": "root" # введите ваш пароль, если он есть
}

conn = None

try:
    # 1. Создаем соединение (connect)
    conn = psycopg2.connect(**db_params)
    
    # 2. Открываем курсор (cursor)
    cur = conn.cursor()
    
    # 3. Выполняем любой SQL-запрос (execute)
    # Например, выведем список категорий из нашей таблицы товаров
    cur.execute("SELECT DISTINCT category FROM products;")
    
    # Получаем результат
    results = cur.fetchall()
    
    print("Соединение установлено успешно!")
    print("Список категорий из базы:")
    for row in results:
        print(f"- {row[0]}")

except Exception as error:
    # Обработка ошибок, чтобы программа не «упала»
    print(f"Ошибка при работе с PostgreSQL: {error}")

finally:
    # 5. Закрываем всё за собой (курсор и соединение)
    if conn:
        cur.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто.")