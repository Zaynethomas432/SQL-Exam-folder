# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate
from easygui import *

# This is the filename of the database to be used
DB_NAME = 'music_lessons.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

# This is the filename of the database to be used
DB_NAME = 'graphics_database.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" graphics_card "
           "LEFT JOIN processors ON graphics_card.processor_id = processors.processor_id "
           "LEFT JOIN manufacturer ON graphics_card.manufacturer_id = manufacturer.manufacturer_id "
           "LEFT JOIN gb_size ON graphics_card.gb_size_id = gb_size.gb_size_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()
      
menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the graphics cards database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: The best graphics cards by NVIDIA\n'
                        'B: Cheap but fast graphics cards\n'
                        'C: Cheap graphics cards that give you the best "bang for your buck"\n'
                        'D: NVIDIA graphics cards with "Blackwell" architecture that perform the best\n'
                        'E: The top 10 best graphics cards, ignoring the price.\n'
                        'F: All graphics card from a certain company, ordered by the best of that company\n'
                        'G: All data\n'
                        'Z: Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
         print_query('best nvidia')
    if menu_choice == 'B':
         print_query('cheap fast cards')
    if menu_choice == 'C':
         print_query('good cheap cards')                 
    if menu_choice == 'D':
         print_query('good GB cards')   
    if menu_choice == 'E':
         print_query('top 10') 
    if menu_choice == 'F':
         company = input("What company's graphics cards do you want to see(NVIDIA, AMD, Intel)? ")
         print_parameter_query("graph_card, processor, cores, tmus, rops, mem_size_gb, bandwidth_gbs, clock_spd_mhz,boost_spd_mhz, fp32_tflops, price", "manufacturer = ? ORDER BY fp32_tflops DESC",company)  
