# Premise: If, five years from now, the sum E of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum E of their ages will be less than 71, how old is Stephanie?
# Golden Label: entailment

sum_ages_future_premise = 51
sum_ages_future_hypothesis = 71

# the hypothesis refers to the future sum of their ages mentioned in the premise
if sum_ages_future_hypothesis <= sum_ages_future_premise:
    # check if the estimate of 'sum_ages_future_hypothesis' contradicts the sum of ages in the premise
    label = "contradiction"
elif sum_ages_future_hypothesis > sum_ages_future_premise:
    # the hypothesis proposes a larger sum of ages than the premise
    # as the premise provides a specific sum, a larger sum cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

