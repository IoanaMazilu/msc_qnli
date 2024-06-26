david_investment_time_premise = 6
david_investment_time_hypothesis = 3
xavier_investment_time_premise = 8
xavier_investment_time_hypothesis = 8

# the hypothesis talks about the time of investment for David and Xavier, also referenced in the premise

if david_investment_time_hypothesis != david_investment_time_premise:
    # check if the investment time for David in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif xavier_investment_time_hypothesis != xavier_investment_time_premise:
    # check if the investment time for Xavier in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
