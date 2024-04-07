# Premise: There are 25 stations between Delhi and Chennai.
# Hypothesis: There are less than 85 stations between Delhi and Chennai.
# Golden Label: entailment

stations_premise = 25
stations_hypothesis = 85

# the hypothesis refers to the number of stations between Delhi and Chennai mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the exact number of stations 'stations_premise'
    label = "contradiction"
elif stations_premise != stations_hypothesis:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

