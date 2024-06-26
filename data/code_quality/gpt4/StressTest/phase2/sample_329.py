amount_premise = 3900
amount_hypothesis = 3900
interest_rate = 0.06

# the hypothesis refers to the amount from Anwar and the interest rate mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the estimate of 'less than amount_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
