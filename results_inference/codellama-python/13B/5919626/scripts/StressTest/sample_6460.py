man_money_premise = 1000
man_money_hypothesis = 1000

# the hypothesis talks about the same amount of money as the premise
if man_money_hypothesis!= man_money_premise:
    # check if the hypothesis value contradicts the estimate of'man_money_premise'
    label = "contradiction"
else:
    # the premise and hypothesis values are the same
    # we can infer entailment
    label = "entailment"

print(label)
