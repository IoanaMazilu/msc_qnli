baseball_fans_premise = 652
baseball_fans_hypothesis = 352

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the estimate of 'baseball_fans_hypothesis' contradicts the number of baseball fans in the premise
    label = "contradiction"
else:
    # the hypothesis value doesn't contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
