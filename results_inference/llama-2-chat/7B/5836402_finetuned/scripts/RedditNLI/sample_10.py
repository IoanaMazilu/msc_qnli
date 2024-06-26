exchange_rate_premise = 65.36
exchange_rate_hypothesis = 68.19
points_premise = 300
points_hypothesis = 282.50
date_premise = "Tuesday 27 Aug"
date_hypothesis = "Wednesday 28 Aug"

# the hypothesis and premise mention the exchange rate, the points change, and the date of the stock market
if exchange_rate_premise!= exchange_rate_hypothesis:
    # check if the exchange rate in the hypothesis contradicts the exchange rate in the premise
    label = "contradiction"
elif points_hypothesis!= points_premise:
    # check if the points change in the hypothesis contradicts the points change in the premise
    label = "contradiction"
elif date_hypothesis!= date_premise:
    # check if the date in the hypothesis contradicts the date in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
