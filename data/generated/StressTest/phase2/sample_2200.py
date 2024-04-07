# Premise: There are less than 38 stations between Hyderabad and Bangalore.
# Hypothesis: There are 28 stations between Hyderabad and Bangalore.
# Golden Label: neutral

stations_premise = 38
stations_hypothesis = 28

# the hypothesis mentions the number of stations between Hyderabad and Bangalore, also referred to in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

