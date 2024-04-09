first_leg_time_premise = 38
first_leg_time_hypothesis = 28

# the hypothesis refers to the time Dawson took to run the first leg of the course, also mentioned in the premise
if first_leg_time_premise <= first_leg_time_hypothesis:
    # check if the time in the premise contradicts the hypothesis estimate of more than 'first_leg_time_hypothesis'
    label = "contradiction"
else:
    # if the premise time does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
