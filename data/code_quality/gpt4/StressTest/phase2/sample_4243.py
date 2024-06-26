david_investment_time_premise = 7
david_investment_time_hypothesis = 6
xavier_investment_time_premise = 8
xavier_investment_time_hypothesis = 8

# the hypothesis talks about the investment times of David and Xavier, referenced also in the premise
if david_investment_time_hypothesis >= david_investment_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'david_investment_time_premise' months
    label = "contradiction"
elif xavier_investment_time_hypothesis != xavier_investment_time_premise:
    # check if the investment time of Xavier in the hypothesis contradicts the investment time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
