# Premise: In a friendship gang Angel has 3 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Angel has 7 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gangs_premise = 3
gangs_hypothesis = 7

# the hypothesis is stating a different number of gangs than the premise 
if gangs_premise != gangs_hypothesis:
    # the numbers of gangs Angel has in the premise and hypothesis contradict each other
    label = "contradiction"
else:
    # if the numbers of gangs were equal, we could infer entailment, but that's not the case here
    label = "neutral"

print(label)

