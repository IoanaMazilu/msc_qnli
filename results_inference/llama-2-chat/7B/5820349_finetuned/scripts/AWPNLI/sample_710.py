balls_premise = 378
jugglers_hypothesis = 63.0

# the hypothesis refers to the number of jugglers needed, which can be calculated from the premise
# compute the number of jugglers needed in the premise
jugglers_premise = balls_premise / 6
if jugglers_hypothesis!= jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
