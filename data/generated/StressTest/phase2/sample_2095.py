# Premise: There are less than 78 stations between Kolkatta and Chennai.
# Hypothesis: There are 28 stations between Kolkatta and Chennai.
# Golden Label: neutral

stations_premise = 78
stations_hypothesis = 28

# the hypothesis talks about the number of stations between two places, mentioned also in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

