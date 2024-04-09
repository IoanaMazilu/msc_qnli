efficient_premise = 1.1
efficient_hypothesis = 0.9

# the hypothesis talks about the efficiency of Rosy compared to Mary, referenced also in the premise
if efficient_hypothesis <= efficient_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficient_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency of Rosy compared to Mary
    # any efficiency greater than 'efficient_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
