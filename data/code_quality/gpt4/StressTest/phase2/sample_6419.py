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
