baseball_fans_premise = 720
baseball_fans_hypothesis = 320

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the premise's upper limit
    label = "contradiction"
else:
    # if the number of fans in the hypothesis is less than the upper limit in the premise, it cannot be explicitly entailed from the premise but it doesn't contradict it either
    label = "neutral"

print(label)
