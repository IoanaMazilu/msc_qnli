year_premise = 1997
investment_premise = 10000
rakesh_investment_premise = 35000

year_hypothesis = 1997
investment_hypothesis = 10000
rakesh_investment_hypothesis = 35000

# the hypothesis refers to the year, the investment amount and Rakesh's investment amount mentioned in the premise
if year_hypothesis <= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif investment_hypothesis != investment_premise or rakesh_investment_hypothesis != rakesh_investment_premise:
    # check if the investment amounts in the hypothesis contradict the amounts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
