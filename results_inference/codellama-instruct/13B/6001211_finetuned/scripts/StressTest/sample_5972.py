second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry took to run the second leg of the course, also mentioned in the premise
if second_leg_time_hypothesis!= second_leg_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
