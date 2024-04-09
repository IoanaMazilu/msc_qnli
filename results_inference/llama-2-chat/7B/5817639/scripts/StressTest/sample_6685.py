less_than_80_steps_premise = 80
less_than_80_steps_hypothesis = 60

# the hypothesis talks about the number of steps climbed by Vinod, referenced also in the premise
if less_than_80_steps_hypothesis <= less_than_80_steps_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_80_steps_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps
    # any number of steps less than or equal to 'less_than_80_steps_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
