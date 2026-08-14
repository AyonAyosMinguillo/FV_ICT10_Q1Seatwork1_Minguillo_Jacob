# Python x PyScript

from pyscript import display, document

fullname = 'Jacob Eon Camacho Minguillo' # String
ag3 = 14 # Integer
he1ght = 172.72 # Float
countries_i_wanna_visit = ['Israel', 'Italy', 'Japan'] # List
student_type = False # Boolean
student_profile = { # Dictionary
    'color': 'Cerulean Blue',
    'car_brand': 'Toyota',
    'shoe_size': 9.5,
    'best_friends': 'Jan Cabading, Logan Anaque, and Kendrick Diño',
}
Favorite_fruits = {'Mango na yellow', 'Banana', 'Durian', 'Grape', 'Watermelon'} # Set
Days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') # Tuple

# ALL THE DISPLAYS

profile_str = ", ".join(str(v) for v in student_profile.values())

display(f"Full Name: {fullname}", target="output")
display(f"Age: {ag3}", target="output")
display(f"Height: {he1ght} cm", target="output")
display(f"Countries to Visit: {', '.join(countries_i_wanna_visit)}", target="output")
display(f"Is New Student: {student_type}", target="output")
display(f"Student Profile: {profile_str}", target="output")
display(f"Favorite Fruits: {', '.join(Favorite_fruits)}", target="output")
display(f"Days of the Week: {', '.join(Days_of_the_week)}", target="output")