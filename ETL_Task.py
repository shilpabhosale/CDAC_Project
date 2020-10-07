#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:24:25 2020

@author: student
"""

import pandas as pd
from selenium import webdriver
import tarfile
from hdfs import *
from hdfs import InsecureClient
from hdfs3 import HDFileSystem
from pyhive import hive
import sasl

host_name = "localhost"
port = 10000
user = "hduser"
password = "password"
database = "default"
conn = hive.Connection(host = host_name, port = port, database = database,username=user,auth="NOSASL")
cur = conn.cursor()

class ETLTask1:  
    #downloading Dataset
#    def hiveconn():
#        host_name = "localhost"
#        port = 10000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#        user = "hduser"
#        password = "password"
#        database = "default"
#        conn = hive.Connection(host = host_name, port = port, database = database,username=user,auth="NOSASL")
#        cur = conn.cursor()
    
    def create_Conn():
        driver=webdriver.Firefox(executable_path='/home/student/geckodriver')
        driver.get("https://public.boxcloud.com/d/1/b1!hF5xU9DOWckLWnHkG5ffm1YhCzcT485-UJ2c7IRYd7My_4iK3A6LW3mZAsPTN8Ko86woBbiSCXN_MInA29O3YC-OD-EYJ3BRNKm1CBp7liB9VAnAB-GIzHIGSGAC49K6IekQuw9bzTOhHk24-aECCF3QtXH2WdESOLFXUzpgldPXhDugVnTPNd3DEy66N7VeBxUjjixp1wMUaPWs1A8VyFVPDHnK9yFc0q5Cjpo5WYi3ga4kEWH2ax7Dbr5fgeAvMm7w3B5UK-2N7uEhUajEt_y-ikWkwRyfVzEirWgJW8wBL01vyCEbalW2R227gk6wUcjDv6jsgQ7svqbNFDZu5vkz04EgCDXlaZTi71qM-e6-mZj2GcalfWiBP5_5JqqgC_abXZGnsBkCon1T7PHPEz56Wub1LKWeQDxw3rmkbCE8EaGI6Sw0s7LrzURTF7hK_Krk_449zgmbe8pGUji5swk3vYIY0Xzt-fnw2Xq7U4BXfviqK0Dmoes61cYMrhRNvg2Q3kBxpHsJNKJ_9Lj93RW2CXuLtvFgap7-rTXYTjMSLpCW2ADyD9z4v9SOI-Cr8gQLaRbmyK_J8w0ZHDdt0lAylBBOAtFyKvzBn8FcUMLWA-2YvAo2tj9kM47eSgB4dnztTKcMKrzEKgHNjbWDeLa_ZtPkfpUvZqtNYim4yslT47APuuUEtkD9DmaQ38tQvJcb8GLH6pOhlYmGDwO2IjKIM6y8bRuL0A334e1quxKy6BZiwkgariAJiUCtXP0Te5cTbJJCEgj51TIRog0HSGTuPE5mFwMF9F-xTG2gLy_iZToh8bFACRsGxtKMmKQFUgseih7-soTt5LL2zZVbSIFEgViJs1gB3DeHhppF4wnDFmVODKaisXBx35AulJJ2JyK-n5qS6iiHSaOBGCn9zO5iDdLbTJRByByUvnm2FM6hTk-cMAi6yASJIzUALs7W8DYYEaI3HBbqIRYmyFuXOqOGtdfUzyf-Jn8KTll_AAMWOCR1DoKY8xM9i4Qb0DkLR-lY0XT3Tdlaoh0Wnsz6c0N6AS8by0C6PSZubX7nAQ6WvCooWla3pWJBQQsnxWi4QqSe0FKO5vCescPJGQHcpFc-RhQY-V7tBlcu0p5pZJvG0pis_rG3EiYtA2gD4ahHGStkc2jQMaQjaBbikRSnm38XmjgZWiqWWCI1IGx1xXOUtdmvtZQBlikXSS1PCHVrIDzDCOVSWHDvu9QENcgQy9mSaDZKkJcQEe8gSR6TxRyOU3g_8eTF8AVFs3KvXQstHgQ8zMYWRcCc9WFYplK424E00eE./download")
    def extract_file():
        tf = tarfile.open("/home/student/Downloads/US_Accidents_May19.tar.gz")
        tf.extractall()
    def conn_to_hdfs():
        try:
            file1="/home/student/project/Final/US_Accidents_May19.csv"
        except:
            print("File Not Found")
        hdfsclient=InsecureClient("http://localhost:50070",user="hduser")
        hdfs_path="/project_data2/"
        hdfsclient.upload(hdfs_path,file1)       
    def create_parent_table():
        #PARENT TABLE
        cur.execute("create table US_ACCIDENT_REC12(ID string,Source string,TMC string,Severity int,StartTime timestamp,EndTime timestamp,StartLat float,StartLng float,EndLat float,EndLng float,Distance float,Description string,Number int,Street string,Side string,City string,County string,State string,Zipcode int,Country string,Timezone timestamp,Airport_Code int,Weather_Timestamp timestamp,Temperature float,Wind_Chill float,Humidity int,Pressure float,Visibility int,Wind_Direction string,Wind_Speed float,Precipitation string,Weather_Condition string,Amenity string,Bump string,Crossing string,Give_Way string,Junction string,No_Exit string,Railway string,Roundabout string,Station string,Stop string,Traffic_Calming string,Traffic_Signal string,Turning_Loop string,Sunrise_Sunset string,Civil_Twilight string,Nautical_Twilight string,Astronomical_Twilight string) row format delimited fields terminated by ',' stored as textfile tblproperties ('skip.header.line.count'='1')" )
        cur.execute("LOAD DATA INPATH '/project_data2' INTO TABLE US_ACCIDENT_REC12")  
    def create_road_table():     
        cur.execute("create table US_ROAD_TABLE1 as select COALESCE(Severity,'0'),COALESCE(Amenity,'UNKNOWN'),COALESCE(Bump,'UNKNOWN'),COALESCE(Crossing,'UNKNOWN'),COALESCE(Give_Way,'UNKNOWN'),COALESCE(Junction,'UNKNOWN'),COALESCE(No_Exit,'UNKNOWN'),COALESCE(Railway,'UNKNOWN'),COALESCE(Roundabout,'UNKNOWN'),COALESCE(Station,'UNKNOWN'),COALESCE(Stop,'UNKNOWN'),COALESCE(Traffic_Calming,'UNKNOWN'),COALESCE(Turning_Loop,'UNKNOWN') from US_ACCIDENT_REC12")
        cur.execute('select * from US_ROAD_TABLE1')
        df1=pd.DataFrame(cur.fetchmany(100000),columns=["Severity","Amenity","Bump","Crossing","Give_Way","Junction","No_Exit","Railway","Roundabout","Station","Stop","Traffic_Calming","Turning_Loop"])  
    def create_loc_table():
        cur.execute("create table US_LOC_TABLE1 as select COALESCE(Severity,'0'),coalesce(Street,'UNKNOWN'),coalesce(City,'UNKNOWN'),coalesce(State,'UNKNOWN') from US_ACCIDENT_REC12")
        cur.execute('select * from US_LOC_TABLE1')
        df2=pd.DataFrame(cur.fetchmany(100000),columns=["Severity","Street","City","State"])
    def create_weather_table():
        cur.execute("create table US_WEATHER_TABLE2 as select COALESCE(Severity,'0'),COALESCE(Temperature,'0'),COALESCE(Wind_Chill,'0'),COALESCE(Humidity,'0'),COALESCE(Pressure,'0'),COALESCE(Visibility,'0'),COALESCE(Wind_Speed,'0'),COALESCE(Precipitation,0),COALESCE(Weather_Condition,'UNKNOWN') from US_ACCIDENT_REC12")
        cur.execute('select * from US_WEATHER_TABLE2')
        df3=pd.DataFrame(cur.fetchmany(100000),columns=["Severity","Temperature","Wind_Chill","Humidity","Pressure","Visibility","Wind_Speed","Precipitation","Weather_Condition"])

def mainmth():
    obj1=ETLTask1
    obj1.create_Conn()
    obj1.extract_file()
    obj1.conn_to_hdfs()
    obj1.create_parent_table()
    obj1.create_weather_table()
    obj1.create_loc_table()
mainmth()