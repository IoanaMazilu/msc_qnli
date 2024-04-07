# Premise: If, five years from now, the sum W of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum W of their ages will be less than 71, how old is Stephanie?
# Golden Label: entailment

sum_ages_future_premise = 51
sum_ages_future_hypothesis = 71

# the hypothesis and premise talk about the sum of their ages in the future
if sum_ages_future_hypothesis < sum_ages_future_premise:
    # check if the hypothesis value contradicts the value of 'sum_ages_future_premise'
    label = "contradiction"
elif sum_ages_future_hypothesis == sum_ages_future_premise:
    # check if the hypothesis value can be entailed from the premise
    label = "entailment"
else:
    # any sum of ages greater than 'sum_ages_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

