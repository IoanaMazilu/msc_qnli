profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis talks about the amount of profit Mr Praveen received, referenced also in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of profit
    # any amount of profit greater than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
