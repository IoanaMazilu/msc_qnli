killed_soldiers_premise = 4
killed_soldiers_hypothesis = 5
injured_soldiers_premise = 4
injured_soldiers_hypothesis = 4
killed_civilians_premise = 3
killed_civilians_hypothesis = 1
injured_civilians_premise = 3
injured_civilians_hypothesis = 3

# the hypothesis mentions the number of killed and injured soldiers and civilians, which are also mentioned in the premise
if killed_soldiers_hypothesis!= killed_soldiers_premise:
    # check if the number of killed soldiers in the hypothesis contradicts the number of killed soldiers reported in the premise
    label = "contradiction"
elif injured_soldiers_hypothesis!= injured_soldiers_premise:
    # check if the number of injured soldiers from the hypothesis contradicts the number of injured soldiers in the premise
    label = "contradiction"
elif killed_civilians_hypothesis!= killed_civilians_premise:
    # check if the number of killed civilians from the hypothesis contradicts the number of killed civilians in the premise
    label = "contradiction"
elif injured_civilians_hypothesis!= injured_civilians_premise:
    # check if the number of injured civilians from the hypothesis contradicts the number of injured civilians in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
