second_leg_premise = 7
second_leg_hypothesis = 6

# the hypothesis refers to the time Henry took to run the second leg of the course, which is also mentioned in the premise
if second_leg_premise!= second_leg_hypothesis:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
