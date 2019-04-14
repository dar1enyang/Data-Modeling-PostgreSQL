# DROP TABLES

songplay_table_drop = "drop table if exists songplay_table" 
user_table_drop = "drop table if exists user_table"
song_table_drop = "drop table if exists song_table"
artist_table_drop = "drop table if exists artist_table"
time_table_drop = "drop table if exists time_table"

# CREATE TABLES

# Fact table
songplay_table_create = (""" \
                        create table if not exists songplay_table \
                        (songplay_id SERIAL PRIMARY KEY, \
                        start_time bigint  not null, \
                        user_id int  not null, \
                        level varchar, \
                        song_id varchar , \
                        artist_id varchar , \
                        session_id int, \
                        location varchar, \
                        user_agent varchar); \
                        """)

#Dimension Tables

#users - users in the app
user_table_create = (""" \
                    create table if not exists user_table \
                    (user_id int PRIMARY KEY, \
                    first_name varchar, \
                    last_name varchar, \
                    gender varchar, \
                    level varchar); \
                    """)
#songs - songs in music database
song_table_create = (""" \
                    create table if not exists song_table \
                    (song_id varchar PRIMARY KEY, \
                    title varchar, \
                    artist_id varchar , \
                    year int, \
                    duration numeric); \
                    """)
#artists - artists in music database
artist_table_create = (""" \
                    create table if not exists artist_table \
                    (artist_id varchar PRIMARY KEY, \
                    artist_name varchar, \
                    artist_location varchar, \
                    artist_lattitude numeric, \
                    artist_longitude numeric); \
                    """)
#time - timestamps of records in songplays broken down into specific units
time_table_create = (""" \
                    create table if not exists time_table \
                    (start_time bigint PRIMARY KEY, \
                    hour int, \
                    day int, \
                    week int, \
                    month int, \
                    year int, \
                    weekday varchar); \
                    """)

# INSERT RECORDS
songplay_table_insert = (""" \
                        INSERT INTO songplay_table \
                        (start_time , \
                        user_id , \
                        level , \
                        song_id , \
                        artist_id , \
                        session_id , \
                        location , \
                        user_agent ) \
                        VALUES (%s,%s,%s, %s,%s,%s, %s,%s)
                        """)

user_table_insert = (""" \
                    INSERT INTO user_table \
                    (user_id , \
                    first_name , \
                    last_name , \
                    gender , \
                    level ) \
                    VALUES (%s, %s,%s,%s, %s) \
                    ON CONFLICT (user_id) \
                    DO UPDATE \
                    SET level=excluded.level;
                    """)

song_table_insert = (""" \
                    INSERT INTO song_table \
                    (song_id , \
                    title , \
                    artist_id , \
                    year , \
                    duration) \
                    VALUES (%s, %s,%s,%s, %s)
                    """)

artist_table_insert = (""" \
                    INSERT INTO artist_table \
                    (artist_id , \
                    artist_name , \
                    artist_location , \
                    artist_lattitude , \
                    artist_longitude) \
                    VALUES (%s, %s,%s,%s, %s) \
                    ON CONFLICT (artist_id) \
                    DO NOTHING;""")


time_table_insert = (""" \
                    INSERT INTO time_table \
                    (start_time , \
                    hour , \
                    day , \
                    week , \
                    month , \
                    year , \
                    weekday ) \
                    VALUES (%s, %s,%s,%s, %s,%s,%s) \
                    ON CONFLICT (start_time) \
                    DO NOTHING;""")

# FIND SONGS

song_select = (""" \
                SELECT  song_table.song_id,artist_table.artist_id \
                FROM  song_table \
                JOIN  artist_table \
                on song_table.artist_id=artist_table.artist_id \
                WHERE  song_table.title=%s and artist_table.artist_name=%s \
                and song_table.duration=%s 
                """)


song_select2 = (""" \
                SELECT  song_table.song_id,artist_table.artist_id \
                FROM  song_table \
                JOIN  artist_table \
                on song_table.artist_id=artist_table.artist_id""")
# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop,song_table_drop, time_table_drop,songplay_table_drop]