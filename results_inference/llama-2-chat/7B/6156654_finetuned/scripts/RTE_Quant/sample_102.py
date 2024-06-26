# The hypothesis mentions the same event as the premise, but with different numbers of casualties

killed_premise = 4
killed_hypothesis = 4
wounded_premise = 80
wounded_hypothesis = 80

if killed_premise!= killed_hypothesis:
    # Check if the number of killed in the hypothesis contradicts the number of killed in the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # Check if the number of wounded in the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
