first_leg_premise = 38
first_leg_hypothesis = 68

# the hypothesis talks about the time Dawson runs the first leg of the course, referenced also in the premise
if first_leg_hypothesis!= first_leg_premise:
    # check if the time of the first leg in the hypothesis contradicts the time of the first leg reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
