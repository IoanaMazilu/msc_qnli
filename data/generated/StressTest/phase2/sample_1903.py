# Premise: There are less than 74 stations between Ernakulam and Chennai.
# Hypothesis: There are 24 stations between Ernakulam and Chennai.
# Golden Label: neutral

stations_premise = 74
stations_hypothesis = 24

# the hypothesis talks about the number of stations between Ernakulam and Chennai, referenced also in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
