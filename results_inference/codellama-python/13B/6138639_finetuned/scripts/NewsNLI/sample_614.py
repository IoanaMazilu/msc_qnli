killed_soldiers_premise = 4
killed_soldiers_hypothesis = 5
killed_civilians_premise = 3
killed_civilians_hypothesis = 1

# the hypothesis mentions the number of killed soldiers and civilians, which are also mentioned in the premise
if killed_soldiers_hypothesis!= killed_soldiers_premise:
    # check if the number of killed soldiers in the hypothesis contradicts the number of killed soldiers reported in the premise
    label = "contradiction"
elif killed_civilians_hypothesis!= killed_civilians_premise:
    # check if the number of killed civilians from the hypothesis contradicts the number of killed civilians in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
