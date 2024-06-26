money_given_premise = 40
money_given_hypothesis = 60

# the hypothesis refers to the percentage of money that Jones gave to his wife, mentioned in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif money_given_hypothesis > money_given_premise:
    # the premise explicitly states that Jones gave 'money_given_premise'% of his money
    # so any percentage less than 'money_given_hypothesis' can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
