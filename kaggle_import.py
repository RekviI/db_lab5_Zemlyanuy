import csv
import psycopg2

username = 'Zemlyanuy_Daniel'
password = 'postgres'
database = 'Laboratory5'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'StreamingApplication.csv'

query_01 = '''
CREATE TABLE Person
(
  user_id VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  gender CHAR(10) NOT NULL,
  subscription CHAR(15) NOT NULL,
  PRIMARY KEY (user_id)
)
'''
query_02 = '''
CREATE TABLE Video
(
  genre CHAR(15) NOT NULL,
  video_url VARCHAR(100) NOT NULL,
  PRIMARY KEY (video_url)
)
'''
query_03 = '''
CREATE TABLE Device
(
  watched_time FLOAT NOT NULL,
  device_id VARCHAR(50) NOT NULL,
  device_type CHAR(15) NOT NULL,
  user_id VARCHAR(50) NOT NULL,
  video_url VARCHAR(100) NOT NULL,
  PRIMARY KEY (device_id),
  FOREIGN KEY (user_id) REFERENCES Person(user_id),
  FOREIGN KEY (video_url) REFERENCES Video(video_url)
)
'''

query_1 = '''
INSERT INTO person (user_id, age, gender, subscription) VALUES (%s, %s, %s, %s)
'''
query_2 = '''
INSERT INTO video (video_url, genre) VALUES (%s, %s)
'''
query_3 = '''
INSERT INTO device (device_id, watched_time, device_type, user_id, video_url) VALUES (%s, %s, %s, %s, %s)
'''

with open(INPUT_CSV_FILE, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    conn = psycopg2.connect(user=username, password=password, database=database, host=host, port=port)
    cursor = conn.cursor()
    cursor.execute(query_01)
    cursor.execute(query_02)
    cursor.execute(query_03)

    for row in csvreader:
        user_id = row[0]
        age = row[6]
        gender = row[7]
        subscription = row[8]

        cursor.execute(query_1, (user_id, age, gender, subscription))

    csvfile.seek(0)
    next(csvreader)

    for row in csvreader:
        genre = row[5]
        video_url = row[1]
        cursor.execute(query_2, (video_url, genre))

    csvfile.seek(0)
    next(csvreader)

    for row in csvreader:
        user_id = row[0]
        video_url = row[1]
        watched_time = row[4]
        device_id = row[2]
        device_type = row[9]
        cursor.execute(query_3, (device_id, watched_time, device_type, user_id, video_url))

    conn.commit()
    cursor.close()
    conn.close()
