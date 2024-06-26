sold_value_premise = 450
sold_value_hypothesis = 750

# the hypothesis talks about the value of something sold, referenced also in the premise
if sold_value_hypothesis <= sold_value_premise:
    # check if the hypothesis value contradicts the estimate of the value sold in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value sold
    # any value greater than'sold_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
