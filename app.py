from models.menu import Menu
from database import Database

"""
    Date:       09/03/2016
    Program:    A small command line blog using mongoDB
"""

__author__ = "Seamus de Cleir"

# Starts the Database IMPORTANT
Database.initialize()

menu = Menu()

menu.run_menu()

