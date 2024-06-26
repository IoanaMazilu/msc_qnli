susan_atkins_premise = 17
susan_atkins_hypothesis = 17

# the hypothesis mentions the number of times Susan Atkins has been denied parole, which is also mentioned in the premise
if susan_atkins_hypothesis!= susan_atkins_premise:
    # check if the number of times Susan Atkins has been denied parole in the hypothesis contradicts the number of times she has been denied parole in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
