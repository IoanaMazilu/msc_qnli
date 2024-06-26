wounded_premise = 0
killed_premise = 0
wounded_hypothesis = 0
killed_hypothesis = 6

if killed_hypothesis!= killed_premise:
    # check if the number of killed in the hypothesis contradicts the number of killed in the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded in the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
