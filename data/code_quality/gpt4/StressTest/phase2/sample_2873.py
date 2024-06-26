baseball_fans_premise = 330
baseball_fans_hypothesis = 330

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis < baseball_fans_premise:
    # check if the condition of 'baseball_fans_hypothesis' being less than 'baseball_fans_premise' is true
    label = "contradiction"
elif baseball_fans_hypothesis > baseball_fans_premise:
    # check if the condition of 'baseball_fans_hypothesis' being more than 'baseball_fans_premise' is true
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
