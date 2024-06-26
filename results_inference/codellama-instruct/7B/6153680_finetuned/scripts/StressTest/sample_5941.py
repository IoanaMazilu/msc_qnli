gang_premise = 2
gang_hypothesis = 5

# the hypothesis talks about the number of gangs Mala has, which is also mentioned in the premise
if gang_hypothesis <= gang_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
