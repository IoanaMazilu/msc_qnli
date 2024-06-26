man_money_premise = 1000
man_money_hypothesis = 1000

# the hypothesis talks about the same amount of money as the premise
if man_money_hypothesis!= man_money_premise:
    # check if the hypothesis value contradicts the estimate of'man_money_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money equal to'man_money_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
