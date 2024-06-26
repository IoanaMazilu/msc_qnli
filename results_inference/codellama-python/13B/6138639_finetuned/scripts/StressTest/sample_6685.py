# define the variables for the premise and hypothesis
steps_premise = 80
steps_hypothesis = 60
time_premise = 40
time_hypothesis = 40

# the hypothesis refers to the number of steps and time mentioned in the premise
if steps_hypothesis >= steps_premise:
    # check if the hypothesis value contradicts the estimate of less than'steps_premise'
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps
    # any number of steps less than'steps_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)