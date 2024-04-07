# Premise: At the end of'n'years, Sandy got back 2 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back less than 2 times the original investment.
# Golden Label: contradiction

investment_return_premise = 2
investment_return_hypothesis = 2

# the hypothesis refers to the return on investment after 'n' years mentioned in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be inferred as entailment
    label = "entailment"

print(label)

