investment_premise = 20000
investment_hypothesis = 20000
investment_year_premise = 1
investment_year_hypothesis = 1

# the hypothesis refers to the investment amount and the number of months, both mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
elif investment_year_hypothesis!= investment_year_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
