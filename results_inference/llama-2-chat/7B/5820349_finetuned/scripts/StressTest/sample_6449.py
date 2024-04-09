years_premise = 5
years_hypothesis = 7

# the hypothesis refers to the time when John will be twice as old as Frank, which is also mentioned in the premise
if years_hypothesis!= years_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
