global_debt_premise = 57e12
global_debt_hypothesis = 57e12
time_period_premise = 7
time_period_hypothesis = 7

# the hypothesis and premise mention the growth of global debt and the time period since the financial crisis
if global_debt_premise!= global_debt_hypothesis:
    # check if the growth of global debt in the hypothesis contradicts the growth of global debt in the premise
    label = "contradiction"
elif time_period_hypothesis!= time_period_premise:
    # check if the time period since the financial crisis in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
