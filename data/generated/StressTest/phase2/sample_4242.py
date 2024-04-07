# Premise: John invests some money at the beginning, David invests double the amount after 6 months, and Xavier invests thrice the amount after 8 months.
# Hypothesis: John invests some money at the beginning, David invests double the amount after less than 7 months, and Xavier invests thrice the amount after 8 months.
# Golden Label: entailment

john_investment_premise = 1
david_investment_premise = 2
xavier_investment_premise = 3
david_investment_time_premise = 6
xavier_investment_time_premise = 8

john_investment_hypothesis = 1
david_investment_hypothesis = 2
xavier_investment_hypothesis = 3
david_investment_time_hypothesis = 7
xavier_investment_time_hypothesis = 8

# the hypothesis refers to the investments and time frames mentioned in the premise
if john_investment_premise != john_investment_hypothesis or david_investment_premise != david_investment_hypothesis or xavier_investment_premise != xavier_investment_hypothesis:
    # check if the investment amounts in the hypothesis contradict the investment amounts reported in the premise
    label = "contradiction"
elif david_investment_time_hypothesis > david_investment_time_premise:
    # check if the investment time for David in the hypothesis contradicts the investment time for David reported in the premise
    label = "contradiction"
elif xavier_investment_time_hypothesis != xavier_investment_time_premise:
    # check if the investment time for Xavier in the hypothesis contradicts the investment time for Xavier reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

