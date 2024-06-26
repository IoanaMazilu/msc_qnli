mary_investment_premise = 400
harry_investment_premise = 300
mary_investment_hypothesis = 700
harry_investment_hypothesis = 300

# the hypothesis refers to the investments made by Mary and Harry, which are also mentioned in the premise
if mary_investment_hypothesis <= mary_investment_premise:
    # check if the amount invested by Mary in the hypothesis contradicts the estimate of 'more than mary_investment_premise'
    label = "contradiction"
elif harry_investment_hypothesis != harry_investment_premise:
    # check if the amount invested by Harry in the hypothesis contradicts the amount invested by Harry in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment made by Mary
    # any investment made by Mary greater than 'mary_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
