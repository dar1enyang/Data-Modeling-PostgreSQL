# Introduction

Knowing how customers interact with the platform via app or website is very important to the music streaming business. 

The analytics people are particularly interested in understanding what songs users are listening to.

Currently, there is no easy way to directly query the data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.



# Project Objective

Design and structure data to make it available to the others in the team. So they can make use of it easily.

Throughout this project, I have completed the following tasks:

1. Created a Postgres database with tables designed to optimize queries on song play analysis
2. Built an ETL pipeline that transfers data from two directories into tables in Postgres using Python and SQL



# Technology 

<p align="middle">
  <img src="https://ws2.sinaimg.cn/large/006tNc79ly1g2bsurr78cj306605e0t2.jpg" />
  <img src="https://ws2.sinaimg.cn/large/006tNc79ly1g2bsv06jf3j30gp05njtd.jpg" />

# Explore the dataset

##### 1. Song Dataset

The first dataset is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```txt
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```json
{"num_songs": 1, 
 "artist_id": "ARJIE2Y1187B994AB7", 
 "artist_latitude": null, 
 "artist_longitude": null, 
 "artist_location": "", 
 "artist_name": "Line Renaud", 
 "song_id": "SOUPIRU12A6D4FA1E1", 
 "title": "Der Kleine Dompfaff", 
 "duration": 152.92036, 
 "year": 0}
```

##### 2. Log Dataset

The second dataset consists of log files in JSON format. These describe app activity logs from a music streaming app based on specified configurations.

The log files in the dataset are partitioned by year and month. 

For example, here are filepaths to two files in this dataset.

```txt
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

![](https://ws3.sinaimg.cn/large/006tNc79ly1g2bsvkkb18j316d0cstbp.jpg)

# Methodology 

### Star Schema Design - Optimized for queries on song play analysis

![](https://ws2.sinaimg.cn/large/006tNc79ly1g2bsvrjxy1j30hg0c2aax.jpg)



# How to use this project

How to install and set up Postgres locally in case you want to follow along with the project on your local machine. This [link](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb) provides it for MacOs. It goes through configuring Postgres, creating users, creating databases using the psql utility.

Perform ETL development in `etl.ipynb` and `test.ipynb`

1. Run `create_tables.py` to create database and tables 

   (Alter queries if you want in `sql_queries.py`)

2. Run `etl.py` to perform the complete ETL pipeline
