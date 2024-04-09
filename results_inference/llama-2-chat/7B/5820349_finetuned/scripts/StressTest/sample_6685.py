steps_climbed_premise = 80
steps_climbed_hypothesis = 60
time_taken = 40

# the hypothesis talks about the number of steps climbed by Vinod, referenced also in the premise
if steps_climbed_hypothesis >= steps_climbed_premise:
    # check if the hypothesis value contradicts the estimate of less than'steps_climbed_premise'
    label = "contradiction"
elif steps_climbed_hypothesis < steps_climbed_premise:
    # the premise gives only an estimate for the number of steps
    # any number of steps less than'steps_climbed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
