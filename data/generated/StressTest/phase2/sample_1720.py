# Premise: There are less than 38 stations between Ernakulam and Chennai.
# Hypothesis: There are 18 stations between Ernakulam and Chennai.
# Golden Label: neutral

stations_premise = 38
stations_hypothesis = 18

# the hypothesis talks about the number of stations between the same cities mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

