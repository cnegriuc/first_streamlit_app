import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page                   
streamlit.dataframe(fruits_to_show)
#############################################
# New section to dispaly api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the sceen as a atble 
streamlit.dataframe(fruityvice_normalized)


# snowflake connector 

#import the snowflake connector library as sf
import snowflake.connector as sf

# Creating the context object
# -----------------------------------

print("1. Creating Snowflake Connection/Context Object")

# it is simple authentication - using user-id & pwd
sf_conn_obj = sf.connect(
    user = 'conegriuc',
    password ='Training123!!',
    account = 'vx06814.ca-central-1',
    warehouse = 'COMPUTE_WH',
    database = 'TEST_DB',
    schema = 'TEST_SCHEMA'
)

print("2. Connetion established successfully ")
print("2.1 Object => " , type(sf_conn_obj))
print("2.2 Account => " , sf_conn_obj.account)
print("2.3 Database => " , sf_conn_obj.database)
print("2.4 Schema => " , sf_conn_obj.schema)
print("2.5 Warehouse => " , sf_conn_obj.warehouse)
print("2.6 Application => " , sf_conn_obj.application)

# -------------------------------------------------
print("3. From context, getting the cursor object")
sf_cursor_obj = sf_conn_obj.cursor()

print("3.1 Object => " , type(sf_cursor_obj))

# -------------------------------------------------
print("4. Ready to execute a query on cursor object")
try:
    # execute any kind of query via execute method
    sf_cursor_obj.execute("select \
    current_database(), current_schema(), current_warehouse(), \
    current_version(), current_account(), current_client()")

    # Same cursor object help to fetch data
    one_row = sf_cursor_obj.fetchone()
    print("Current DB => ",one_row[0])
    print("Current Schema => ",one_row[1])
    print("Current Warehouse => ",one_row[2])
    print("Current Version => ",one_row[3])
    print("Current Account => ",one_row[4])
    print("Current Client => ",one_row[5])
finally:
    #closing the connection object
    sf_cursor_obj.close()
    
# closing the context object
sf_conn_obj.close()
