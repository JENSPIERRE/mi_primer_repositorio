from django.http import HttpResponse
import psycopg2

def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp VALUES        ('7365','HUGO','OFICINISTA', "
                    "'7903',date    '1980-12-17','800.00',NULL,'20');")
    return HttpResponse("Insertado")

def select(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    return HttpResponse(cursor.fetchall())




