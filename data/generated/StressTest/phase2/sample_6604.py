# Premise: At the end of'n'years, Sandy got back less than 3 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back 2 times the original investment.
# Golden Label: neutral

returned_investment_premise = 3
returned_investment_hypothesis = 2

# the hypothesis talks about the amount Sandy got back after 'n' years, referenced also in the premise
if returned_investment_hypothesis >= returned_investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'returned_investment_premise'
    label = "contradiction"
elif returned_investment_hypothesis < returned_investment_premise:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

