# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for less than 6 years at 4% per annum simple interest?
# Golden Label: entailment

years_premise = 2
years_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis talks about the number of years and interest rate in a situation, which is also referenced in the premise
if years_hypothesis < years_premise:
    # check if the 'years_hypothesis' contradicts the number of years mentioned in the 'years_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but cannot be explicitly entailed from the premise
    # since "less than 6 years" includes 2 years but also other possible values
    label = "neutral"

print(label)

