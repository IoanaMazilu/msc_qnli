# Premise: If, five years from now, the sum Q of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum Q of their ages will be more than 31, how old is Stephanie?
# Golden Label: entailment

sum_ages_future_premise = 51
sum_ages_future_hypothesis = 31

# the hypothesis refers to the future sum of their ages mentioned in the premise
if sum_ages_future_premise < sum_ages_future_hypothesis:
    # check if the estimate of 'sum_ages_future_hypothesis' contradicts the sum of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

