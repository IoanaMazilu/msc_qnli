baseball_fans_premise = 320
baseball_fans_hypothesis = 720

# the hypothesis refers to the number of baseball fans in the town, mentioned in the premise
if baseball_fans_premise >= baseball_fans_hypothesis:
    # check if the estimate of 'baseball_fans_hypothesis' contradicts the number of baseball fans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
