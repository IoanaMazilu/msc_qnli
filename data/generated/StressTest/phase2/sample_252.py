# Premise: If, five years from now, the sum R of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum R of their ages will be less than 81, how old is Stephanie?
# Golden Label: entailment

sum_ages_future_premise = 51
sum_ages_future_hypothesis = 81

# the hypothesis talks about the sum of ages in the future, referenced in the premise
if sum_ages_future_hypothesis < sum_ages_future_premise:
    # check if the hypothesis value contradicts the sum of ages in the premise
    label = "contradiction"
elif sum_ages_future_hypothesis == sum_ages_future_premise:
    # if the sum of ages in the hypothesis equals the sum of ages in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives a specific value for the sum of ages
    # any sum of ages greater than 'sum_ages_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

