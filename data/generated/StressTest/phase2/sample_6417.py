# Premise: In a friendship gang Angel has 3 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Angel has less than 7 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: entailment

gang_premise = 3
gang_hypothesis = 7

# The hypothesis refers to the number of gangs Angel has, which is also mentioned in the premise.
if gang_premise >= gang_hypothesis:
    # Check if the hypothesis number contradicts the number of gangs Angel has in the premise.
    label = "contradiction"
else:
    # If the hypothesis number does not contradict the premise one, we can infer entailment.
    label = "entailment"

print(label)

