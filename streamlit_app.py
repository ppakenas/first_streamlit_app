import streamlit
streamlit.title('Test App')

streamlit.header('Cyber Ponies')
streamlit.text('date placeholder')
streamlit.text('🥣 🥗 🐔 🥑🍞')

streamlit.header('Today\'s Picks')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# Display the table on the page.

streamlit.dataframe(fruits_to_show)



#New section to display fruityvice api response
streamlit.header('Horse Race Advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())  #simply writes data to the screen

#takes json version and normalize
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output as a table
streamlit.dataframe(fruityvice_normalized)
