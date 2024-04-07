# Premise: There are 24 stations between Ernakulam and Chennai.
# Hypothesis: There are less than 74 stations between Ernakulam and Chennai.
# Golden Label: entailment

stations_premise = 24
stations_hypothesis = 74

# the hypothesis talks about the number of stations between two places, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the exact number 'stations_premise'
    label = "contradiction"
else:
    # the premise gives an exact number for the stations
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

