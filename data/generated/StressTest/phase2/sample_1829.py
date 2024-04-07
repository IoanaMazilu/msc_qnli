# Premise: There are 15 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 15 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 15
stations_hypothesis = 15

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of less than 'stations_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number for the stations
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

