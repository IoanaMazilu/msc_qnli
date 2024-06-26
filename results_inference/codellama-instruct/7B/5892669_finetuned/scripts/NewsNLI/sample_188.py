denied_parole_premise = 17
denied_parole_hypothesis = 17

# the hypothesis mentions the number of times Susan Atkins has been denied parole, which is also referenced in the premise
if denied_parole_hypothesis!= denied_parole_premise:
    # check if the number of denied parole in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
