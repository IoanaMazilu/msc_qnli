 gang_premise = 3
gang_hypothesis = 7

# the hypothesis refers to the number of gangs Angel has, which is also mentioned in the premise
if gang_hypothesis!= gang_premise:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the number of gangs in the hypothesis does not contradict the number of gangs in the premise, we can infer entailment
    label = "entailment"

print(label)
