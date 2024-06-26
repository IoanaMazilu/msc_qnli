y_premise = 560
shirts_bought_premise = 160

# the hypothesis talks about the number of shirts bought by Vijay, which is also mentioned in the premise
if shirts_bought_premise >= 560:
    # check if the hypothesis value contradicts the estimate of less than'shirts_bought_premise'
    label = "contradiction"
elif shirts_bought_premise < 560:
    # the premise gives only an estimate for the number of shirts bought
    # any number of shirts less than'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
