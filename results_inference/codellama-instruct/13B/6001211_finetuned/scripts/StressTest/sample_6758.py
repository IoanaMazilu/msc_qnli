time_premise = 8
time_hypothesis = 6

# the hypothesis refers to the time Tom goes, which is also mentioned in the premise
if time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
