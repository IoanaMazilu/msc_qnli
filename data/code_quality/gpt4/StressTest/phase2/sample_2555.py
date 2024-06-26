sum_ages_future_premise = 51
sum_ages_future_hypothesis = 51

# the hypothesis refers to the sum of their ages five years from now, mentioned in the premise
if sum_ages_future_hypothesis < sum_ages_future_premise:
    # check if the hypothesis' value contradicts the sum of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis' value does not contradict the premise's value, we can infer entailment
    label = "entailment"

print(label)
