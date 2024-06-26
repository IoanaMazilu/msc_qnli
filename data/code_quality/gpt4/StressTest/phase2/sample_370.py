baseball_fans_premise = 560
baseball_fans_hypothesis = 360

# the hypothesis refers to the same town's baseball fans mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the estimate of less than 'baseball_fans_premise'
    label = "contradiction"
else:
    # if the number of baseball fans in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
