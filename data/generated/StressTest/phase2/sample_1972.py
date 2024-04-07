# Premise: There are less than 78 stations between Hyderabad and Bangalore.
# Hypothesis: There are 18 stations between Hyderabad and Bangalore.
# Golden Label: neutral

stations_premise = 78
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, also mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the premise's estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

