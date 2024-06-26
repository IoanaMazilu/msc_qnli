shirts_bought_premise = 160
shirts_bought_hypothesis = 460

# the hypothesis talks about the number of shirts bought by Vijay, which is also referenced in the premise.
if shirts_bought_hypothesis < shirts_bought_premise:
    # check if the hypothesis value contradicts the exact number of 'shirts_bought_premise' bought by Vijay
    label = "contradiction"
elif shirts_bought_hypothesis == shirts_bought_premise:
    # if the hypothesis value is equal to the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an exact number for the shirts bought by Vijay
    # any number of shirts less than 'shirts_bought_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
