balls_premise = 378
juggler_capacity_premise = 6
jugglers_needed_hypothesis = 63.0

# the hypothesis refers to the number of jugglers, which is derived from the number of balls and the juggler's capacity in the premise
# compute the number of jugglers needed according to the premise
jugglers_needed_premise = balls_premise / juggler_capacity_premise

if jugglers_needed_hypothesis != jugglers_needed_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
