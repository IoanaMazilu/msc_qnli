# Premise: In 1998, Mr Shivkumar invested another additional amount of 10000 and Mr Suresh joined them with an amount of 35000.
# Hypothesis: In less than 1998, Mr Shivkumar invested another additional amount of 10000 and Mr Suresh joined them with an amount of 35000.
# Golden Label: contradiction

investment_year_premise = 1998
investment_year_hypothesis = 1998
shivkumar_investment_premise = 10000
shivkumar_investment_hypothesis = 10000
suresh_investment_premise = 35000
suresh_investment_hypothesis = 35000

# the hypothesis refers to the year of the investment and the amount invested by Shivkumar and Suresh, mentioned in the premise
if investment_year_hypothesis >= investment_year_premise:
    # check if the investment year in hypothesis contradicts the year of investment in the premise
    label = "contradiction"
elif shivkumar_investment_hypothesis != shivkumar_investment_premise or suresh_investment_hypothesis != suresh_investment_premise:
    # check if the amount invested by Shivkumar or Suresh in the hypothesis contradicts the amount invested reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

