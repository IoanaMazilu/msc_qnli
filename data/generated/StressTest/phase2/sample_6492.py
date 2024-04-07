# Premise: If Dana gives her parents 3% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents less than 7% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: entailment

repayment_rate_premise = 3
repayment_rate_hypothesis = 7

# the hypothesis refers to the repayment rate, also mentioned in the premise
if repayment_rate_hypothesis <= repayment_rate_premise:
    # check if the 'repayment_rate_hypothesis' contradicts the repayment rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact repayment rate
    # any repayment rate greater than 'repayment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

