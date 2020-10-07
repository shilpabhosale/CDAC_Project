                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:26:35 2020

@author: student
"""

from ETL_Task import ETLTask1
from Algorithm_Implementation import AccidentAlgorithm

def main_mthd():
    
#ETL File
#    obj2=ETLTask1
#    obj2.createConn()
#    obj2.extractfile()
#    obj2.conn_to_hdfs()
#    
    obj1=ETLTask1
    obj1.create_Conn()
    obj1.extract_file()
    obj1.conn_to_hdfs()
    obj1.create_parent_table()
    obj1.create_weather_table()
    obj1.create_loc_table()
    obj1.create_road_table()
    
    
#Algorithm Implementaion
#    obj1=AccidentAlgorithm
#    obj1.Create_ParentTab()
#    obj1.Based_on_Time()
#    obj1.Based_on_road()
#    
    
    obj1= AccidentAlgorithm
    obj1.based_on_weather()
    obj1.based_on_location()
    obj1.based_on_road()
main_mthd()