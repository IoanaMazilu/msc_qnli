steps_climbed_premise = 80
steps_climbed_hypothesis = 60
time_premise = 40
time_hypothesis = 40

# the hypothesis refers to the number of steps climbed by Vinod and the time taken, both mentioned in the premise
if steps_climbed_hypothesis >= steps_climbed_premise:
    # check if the number of steps climbed in the hypothesis contradicts the premise estimate of less than'steps_climbed_premise'
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time taken in the hypothesis contradicts the time taken as per the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps climbed
    # any number of steps less than'steps_climbed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
