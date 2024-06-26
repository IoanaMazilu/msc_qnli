wounded_premise = 1000
killed_hypothesis = 6

# check if the number of killed in the hypothesis contradicts the number of killed in the premise
if killed_hypothesis!= killed_premise:
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded in the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
