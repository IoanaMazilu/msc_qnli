balls_premise = 378
jugglers_hypothesis = 63.0

# compare the number of balls in the premise and hypothesis
if balls_premise!= jugglers_hypothesis:
    # check if the number of balls in the hypothesis contradicts the number of balls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
