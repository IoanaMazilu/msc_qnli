baseball_fans_premise = 352
baseball_fans_hypothesis = 652

# the hypothesis refers to the number of baseball fans in the town, mentioned in the premise
if baseball_fans_premise >= baseball_fans_hypothesis:
    # check if the number of baseball fans in the premise contradicts the estimate of less than 'baseball_fans_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the number of baseball fans
    # any number of fans less than 'baseball_fans_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)