sailors_premise = 15
sailors_hypothesis = 15
damage_premise = "extensive"
damage_hypothesis = 2

# the hypothesis mentions the number of sailors hurt and the damage caused, which are also mentioned in the premise
if sailors_hypothesis!= sailors_premise:
    # check if the number of sailors in the hypothesis contradicts the number of sailors in the premise
    label = "contradiction"
elif damage_hypothesis!= damage_premise:
    # check if the damage in the hypothesis contradicts the damage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
