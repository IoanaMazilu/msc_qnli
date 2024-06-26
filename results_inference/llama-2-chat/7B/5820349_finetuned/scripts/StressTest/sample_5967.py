first_leg_time_premise = 38
first_leg_time_hypothesis = 28

# the hypothesis refers to the time Dawson took to run the first leg of the course, which is also mentioned in the premise
if first_leg_time_premise <= first_leg_time_hypothesis:
    # check if the actual time taken by Dawson contradicts the estimate of 'first_leg_time_hypothesis'
    label = "contradiction"
else:
    # if the actual time taken by Dawson does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
