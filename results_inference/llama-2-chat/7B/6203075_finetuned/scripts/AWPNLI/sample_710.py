balls_premise = 378
jugglers_hypothesis = 63.0
jugglers_premise = 1.0
balls_per_juggler_premise = 6

# the hypothesis refers to the number of jugglers, which can be calculated from the premise
# compute the number of jugglers in the premise
jugglers_premise = balls_premise / jugglers_premise

if jugglers_hypothesis!= jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
