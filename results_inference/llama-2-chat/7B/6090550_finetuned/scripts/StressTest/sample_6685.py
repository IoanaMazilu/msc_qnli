y = 60

steps_climbed_premise = 80
time_taken_premise = 40

steps_climbed_hypothesis = 60
time_taken_hypothesis = 40

# the hypothesis talks about the number of steps Vinod climbed and the time taken to climb them
if steps_climbed_hypothesis >= steps_climbed_premise:
    # check if the hypothesis value contradicts the estimate of less than'steps_climbed_premise'
    label = "contradiction"
elif time_taken_hypothesis!= time_taken_premise:
    # check if the time taken in the hypothesis contradicts the time taken in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps
    # any number of steps less than'steps_climbed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

