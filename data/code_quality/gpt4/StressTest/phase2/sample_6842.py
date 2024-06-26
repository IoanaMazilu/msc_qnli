investment_duration_premise = 6
investment_duration_hypothesis = 6
rick_investment_duration_premise = 12
rick_investment_duration_hypothesis = 12

# the hypothesis refers to the same investment duration and Rick's investment duration as the premise
if investment_duration_hypothesis <= investment_duration_premise:
    # check if the hypothesis value contradicts the premise which stated the investment duration as 'investment_duration_premise'
    label = "contradiction"
elif rick_investment_duration_hypothesis != rick_investment_duration_premise:
    # check if the Rick's investment duration in the hypothesis contradicts the Rick's investment duration mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
