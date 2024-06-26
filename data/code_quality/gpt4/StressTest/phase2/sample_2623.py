baseball_fans_premise = 490
baseball_fans_hypothesis = 390

# the hypothesis is about the number of baseball fans in a town, which is also referenced in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the estimate of less than 'baseball_fans_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball fans
    # any number of baseball fans less than 'baseball_fans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
