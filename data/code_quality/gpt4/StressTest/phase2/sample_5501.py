baseball_fans_premise = 320
baseball_fans_hypothesis = 220

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis != baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the number of baseball fans in the premise
    label = "contradiction"
else:
    # if the number of baseball fans in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
