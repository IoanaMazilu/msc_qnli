# Premise: There are less than 23 stations between Hyderabad and Bangalore.
# Hypothesis: There are 13 stations between Hyderabad and Bangalore.
# Golden Label: neutral

stations_between_cities_premise = 23
stations_between_cities_hypothesis = 13

# the hypothesis speaks about the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_between_cities_hypothesis >= stations_between_cities_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_between_cities_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_between_cities_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

