yrs_back_premise = 5
yrs_back_hypothesis = 6

# the hypothesis refers to the time when John was thrice as old as Tom, as mentioned in the premise
if yrs_back_hypothesis!= yrs_back_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
