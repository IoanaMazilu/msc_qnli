# Premise: There are 28 stations between Kolkatta and Chennai.
# Hypothesis: There are less than 78 stations between Kolkatta and Chennai.
# Golden Label: entailment

stations_premise = 28
stations_hypothesis = 78

# the hypothesis refers to the number of stations between two cities mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the exact number of 'stations_premise'
    label = "contradiction"
elif stations_hypothesis > stations_premise:
    # the premise gives an exact number for the stations
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

