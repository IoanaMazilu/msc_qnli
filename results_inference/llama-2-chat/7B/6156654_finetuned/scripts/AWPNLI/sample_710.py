balls_premise = 378
jugglers_hypothesis = 63

# the hypothesis refers to the number of jugglers needed, which can be inferred from the premise
# compute the number of jugglers needed based on the premise
jugglers_premise = balls_premise / 6

if jugglers_hypothesis!= jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
