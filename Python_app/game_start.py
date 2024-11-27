import random

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='m3615virus_alpha',
    user='root',
    password='mexicana',
    autocommit=True
)

#Select from 20 airports for the game
def get_airports():
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
FROM airport
WHERE continent = 'EU'
AND type = 'large_airport'
AND iso_country IN ('FI', 'SE', 'NO', 'EE', 'LV', 'LT', 'PL', 'SK',
                    'HU', 'AT', 'DE', 'CH', 'CZ', 'BE', 'NL',
                    'FR', 'DK', 'GB', 'IE', 'IS')
ORDER BY RAND()
LIMIT 20;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# get all goals
def get_antidotes():
    sql = "SELECT * FROM antidotes";
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def event():
    sql = "SELECT * FROM events";
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def leaderboard():
    sql = "SELECT * FROM leaderboard"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def players():
    sql = "SELECT * FROM players"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def tasks():
    sql = "SELECT * FROM tasks"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# create a new game

def create_game(username):
    health_bar = 10
    current_airport = random.randint(1,20)
    countries_visited = 0
    collected_antidotes = {}
    sql = "INSERT INTO player(username, health_bar, current_airport, countries_visited, collected_antidotes) VALUES (%s, %s, %s, %s, %s)")
    data = (username, health_bar, current_airport, countries_visited, collected_antidotes)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, data)
    conn.commit()


def create_random_task():
    previous_tasks = []
    random_task = random.randint(1,10)
    while random_task in previous_tasks:
        random_task = random.randint(1,10)
    previous_tasks.append(random_task)
    sql = "SELECT * FROM tasks WHERE id = random_task"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    task = cursor.fetchall()
    return task

def create_random_event()
    random_event = random.randint(1,5)
    previous_events = []
    while random_event in previous_events:
        random_event = random.randint(1,5)
    previous_events.append(random_event)
    sql = "SELECT * FROM events WHERE id = random_event"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    event = cursor.fetchall()
    return event

def travel(airport_id):
    task_event = random.randint(1,3)
    if task_event == 1:
        task = create.random_task()
    if task_event == 2:
        task = create_random_event()
    else:
        task = None

