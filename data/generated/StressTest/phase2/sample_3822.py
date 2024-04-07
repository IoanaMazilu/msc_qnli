# Premise: There are 16 stations between Mumbai and Chennai.
# Hypothesis: There are less than 26 stations between Mumbai and Chennai.
# Golden Label: entailment

stations_premise = 16
stations_hypothesis = 26

# the hypothesis refers to the number of stations between Mumbai and Chennai mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the estimate of 'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
elif stations_hypothesis > stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

