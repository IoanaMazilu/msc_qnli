steps_climbed_premise = 80
steps_climbed_hypothesis = 60
time_climbed_premise = 40
time_climbed_hypothesis = 40

# the hypothesis talks about the number of steps climbed and the time taken to climb them, referenced also in the premise
if steps_climbed_hypothesis <= steps_climbed_premise:
    # check if the hypothesis value contradicts the estimate of less than'steps_climbed_premise'
    label = "contradiction"
elif time_climbed_hypothesis!= time_climbed_premise:
    # check if the time taken to climb the steps in the hypothesis contradicts the time taken to climb the steps reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps and the time taken to climb them
    # any number of steps and time taken to climb them consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
