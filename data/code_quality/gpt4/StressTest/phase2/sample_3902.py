stations_premise = 14
stations_hypothesis = 14

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of less than 'stations_premise'
    label = "contradiction"
else:
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
