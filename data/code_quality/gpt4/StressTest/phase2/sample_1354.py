year_premise = 3998
year_hypothesis = 1998
shivkumar_investment_premise = 10000
shivkumar_investment_hypothesis = 10000
suresh_investment_premise = 35000
suresh_investment_hypothesis = 35000

# the hypothesis refers to the investments made by Mr Shivkumar and Mr Suresh, and the year it happened, as mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the estimate of 'year_premise'
    label = "contradiction"
elif shivkumar_investment_hypothesis != shivkumar_investment_premise or suresh_investment_hypothesis != suresh_investment_premise:
    # check if the investment values in the hypothesis contradict the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
