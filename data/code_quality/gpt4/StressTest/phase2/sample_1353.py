year_invested_premise = 1998
year_invested_hypothesis = 3998
shivkumar_investment_premise = 10000
shivkumar_investment_hypothesis = 10000
suresh_investment_premise = 35000
suresh_investment_hypothesis = 35000

# the hypothesis refers to the year of investment, and the amounts invested by Shivkumar and Suresh, mentioned in the premise
if year_invested_hypothesis >= year_invested_premise:
    # check if the year of investment in the hypothesis contradicts the year of investment in the premise
    label = "contradiction"
elif shivkumar_investment_hypothesis != shivkumar_investment_premise or suresh_investment_hypothesis != suresh_investment_premise:
    # check if the amounts invested by Shivkumar and Suresh in the hypothesis contradict the amounts invested by them in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
