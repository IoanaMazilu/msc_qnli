shirts_bought_premise = 160
shirts_bought_hypothesis = 560

# the hypothesis refers to the number of shirts bought by Vijay, mentioned in the premise
if shirts_bought_premise >= shirts_bought_hypothesis:
    # check if the number of shirts bought in the premise contradicts the estimate of less than'shirts_bought_hypothesis'
    label = "contradiction"
elif shirts_bought_premise < shirts_bought_hypothesis:
    # if the number of shirts bought in the premise is less than'shirts_bought_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if the premise value does not contradict or can be explicitly entailed from the hypothesis, the relation is neutral
    label = "neutral"

print(label)
