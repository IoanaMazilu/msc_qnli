# Premise: There are less than 77 stations between Hyderabad and Bangalore.
# Hypothesis: There are 17 stations between Hyderabad and Bangalore.
# Golden Label: neutral

stations_premise = 77
stations_hypothesis = 17

# the hypothesis refers to the number of stations between two cities mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

