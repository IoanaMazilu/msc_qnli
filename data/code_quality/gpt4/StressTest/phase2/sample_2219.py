gang_premise = 8
gang_hypothesis = 5

# The hypothesis refers to the number of gangs Andrew has, mentioned also in the premise
if gang_hypothesis != gang_premise:
    # if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # The premise and hypothesis are same
    label = "entailment"

print(label)
