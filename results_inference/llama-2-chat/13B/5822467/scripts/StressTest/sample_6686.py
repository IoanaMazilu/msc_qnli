steps_premise = 60
steps_hypothesis = 80
time_premise = 40

# the hypothesis talks about the number of steps climbed and the time taken, both mentioned in the premise
if steps_hypothesis <= steps_premise:
    # check if the hypothesis value contradicts the estimate of'steps_premise'
    label = "contradiction"
elif time_premise!= time_hypothesis:
    # check if the time taken in the hypothesis contradicts the time taken in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps climbed and the time taken
    # any number of steps greater than'steps_premise' and time taken consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
