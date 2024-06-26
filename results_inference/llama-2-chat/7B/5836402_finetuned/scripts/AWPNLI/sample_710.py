balls_premise = 378
jugglers_hypothesis = 63.0

# the hypothesis refers to the number of jugglers needed, which is related to the number of balls in the premise
# compute the number of balls per juggler in the premise
balls_per_jugglers_premise = balls_premise / 1.0
if jugglers_hypothesis!= balls_per_jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of balls per juggler from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
