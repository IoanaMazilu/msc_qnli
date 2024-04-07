# Premise: There are more than 22 stations between Ernakulam and Chennai.
# Hypothesis: There are 32 stations between Ernakulam and Chennai.
# Golden Label: neutral

stations_premise = 22
stations_hypothesis = 32

# the hypothesis talks about the number of stations between Ernakulam and Chennai, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of more than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

