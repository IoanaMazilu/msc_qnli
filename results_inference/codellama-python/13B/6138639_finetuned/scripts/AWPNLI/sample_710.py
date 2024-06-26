balls_premise = 378
juggler_premise = 1
balls_per_juggler_premise = 6
jugglers_hypothesis = 63.0

# the hypothesis refers to the number of jugglers, which can be computed from the premise
# compute the number of jugglers in the premise
jugglers_premise = balls_premise / balls_per_juggler_premise
if jugglers_hypothesis!= jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
