saving_decrease_premise = 80
saving_decrease_hypothesis = 30

# the hypothesis talks about the decrease in savings due to loan payment, referenced also in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_decrease_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the decrease in savings
    # any decrease less than'saving_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
