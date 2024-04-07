# Premise: If, five years from now, the sum G of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum G of their ages will be less than 71, how old is Stephanie?
# Golden Label: entailment

# variables for sum of ages in the future
sum_ages_future_premise = 51
sum_ages_future_hypothesis = 71

# the hypothesis refers to the sum of their ages in the future, just like the premise
if sum_ages_future_hypothesis < sum_ages_future_premise:
    # check if the estimate of 'sum_ages_future_hypothesis' contradicts the sum of ages in the premise
    label = "contradiction"
elif sum_ages_future_premise != sum_ages_future_hypothesis:
    # if the sum of ages in the future in the hypothesis is greater than the sum in the premise, we can infer the relation as neutral
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

