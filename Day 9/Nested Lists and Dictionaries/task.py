travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# See if you can figure out how to print out "Lille" from the nested List called travel_log
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.
print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Figure out how to print out "Stuttgart" from the following list:
print(travel_log["Germany"]["cities_visited"][2])