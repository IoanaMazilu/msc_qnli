walking_rate_matthew_premise = 5
walking_rate_matthew_hypothesis = 3
walking_rate_johnny_premise = 4
walking_rate_johnny_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if walking_rate_matthew_hypothesis <= walking_rate_matthew_premise:
    # check if the estimate of 'walking_rate_matthew_hypothesis' contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif walking_rate_johnny_hypothesis!= walking_rate_johnny_premise:
    # check if the number of walked km by Johnny in the hypothesis contradicts the number of walked km reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
