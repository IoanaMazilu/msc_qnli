decrease_premise = 80
decrease_hypothesis = 30

# the hypothesis talks about the decrease in John's Bank's saving amount, referenced also in the premise
if decrease_hypothesis >= decrease_premise:
    # check if the hypothesis value contradicts the estimate of less than 'decrease_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the decrease
    # any decrease less than 'decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
