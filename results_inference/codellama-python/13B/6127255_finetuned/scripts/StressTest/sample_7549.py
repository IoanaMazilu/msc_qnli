saving_decrease_premise = 0.8
saving_decrease_hypothesis = 0.3

# the hypothesis talks about the decrease in saving amount, which is also mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_decrease_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the decrease in saving amount
    # any decrease less than'saving_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
