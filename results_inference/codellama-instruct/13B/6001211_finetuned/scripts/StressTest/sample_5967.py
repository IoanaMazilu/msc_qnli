first_leg_time_premise = 38
first_leg_time_hypothesis = 28

# the hypothesis refers to the time Dawson took to run the first leg of the course, also mentioned in the premise
if first_leg_time_premise <= first_leg_time_hypothesis:
    # check if the time Dawson took to run the first leg in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the time Dawson took to run the first leg in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
