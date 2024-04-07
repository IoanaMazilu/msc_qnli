# Premise: At the end of'n'years, Sandy got back 3 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back less than 8 times the original investment.
# Golden Label: entailment

returned_investment_premise = 3
returned_investment_hypothesis = 8

# the hypothesis talks about the return on Sandy's investment, as referred to in the premise
if returned_investment_hypothesis <= returned_investment_premise:
    # check if the hypothesis value contradicts the estimate of 'returned_investment_premise'
    label = "contradiction"
else:
    # the hypothesis value is greater than 'returned_investment_premise'
    # any return on investment less than 'returned_investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

