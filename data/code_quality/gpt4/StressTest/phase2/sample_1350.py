year_premise = 1997
year_hypothesis = 3997
investment_premise = 10000
investment_hypothesis = 10000
rakesh_investment_premise = 35000
rakesh_investment_hypothesis = 35000

# the hypothesis refers to the investments made, which are also mentioned in the premise
if investment_premise != investment_hypothesis:
    # check if the value of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
elif rakesh_investment_premise != rakesh_investment_hypothesis:
    # check if the value of 'rakesh_investment_hypothesis' contradicts the investment amount made by Mr Rakesh in the premise
    label = "contradiction"
elif year_hypothesis > year_premise:
    # check if the year in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
