profit_premise = 85
profit_hypothesis = 15

# the hypothesis talks about the profit Sally will have to generate by selling each item, referenced also in the premise
if profit_hypothesis >= profit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit 
    # any profit less than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
