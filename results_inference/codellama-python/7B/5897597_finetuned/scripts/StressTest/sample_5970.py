second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry took to run the second leg of the course, mentioned also in the premise
if second_leg_time_premise <= second_leg_time_hypothesis:
    # check if the time in the premise contradicts the estimate of more than'second_leg_time_hypothesis'
    label = "contradiction"
else:
    # if the time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)