distance_cities = 100

# the hypothesis refers to the distance between the two cities
if distance_cities <= distance_cities:
    # check if the estimate of 'distance_cities' contradicts the distance between the two cities in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between the two cities
    # any distance greater than 'distance_cities' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
