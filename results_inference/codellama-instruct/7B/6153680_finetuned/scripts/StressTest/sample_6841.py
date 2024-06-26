investment_time_premise = 7
investment_time_hypothesis = 6
total_investment_premise = 20000
total_investment_hypothesis = 20000

# the hypothesis refers to the investment time and total investment mentioned in the premise
if investment_time_hypothesis >= investment_time_premise:
    # check if the investment time in the hypothesis contradicts the investment time in the premise
    label = "contradiction"
elif total_investment_hypothesis!= total_investment_premise:
    # check if the total investment in the hypothesis contradicts the total investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
