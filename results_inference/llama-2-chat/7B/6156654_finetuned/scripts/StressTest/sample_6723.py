total_amount_premise = 3600
total_amount_hypothesis = 1600
interest_rate = 6

# the hypothesis refers to the total amount of money lent by Anwar, which is also mentioned in the premise
if total_amount_hypothesis <= total_amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate!= 6:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
