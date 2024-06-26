killed_premise = 3
killed_hypothesis = 7

# check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
if killed_hypothesis!= killed_premise:
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
