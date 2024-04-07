# Premise: If Jim pays 30 dollars, how much will Joe have to pay?
# Hypothesis: If Jim pays less than 70 dollars, how much will Joe have to pay?
# Golden Label: entailment

jim_pay_premise = 30
jim_pay_hypothesis = 70

# the hypothesis refers to the payment amount of Jim mentioned in the premise
if jim_pay_premise >= jim_pay_hypothesis:
    # check if the 'jim_pay_premise' contradicts the condition of 'jim_pay_hypothesis' being less
    label = "contradiction"
elif jim_pay_premise < jim_pay_hypothesis:
    # if 'jim_pay_premise' is less than 'jim_pay_hypothesis', it is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

