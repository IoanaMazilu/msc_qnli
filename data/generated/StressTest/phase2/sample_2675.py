# Premise: If, five years from now, the sum E of their ages will be 51, how old is Stephanie?
# Hypothesis: If, five years from now, the sum E of their ages will be 21, how old is Stephanie?
# Golden Label: contradiction

sum_ages_future_premise = 51
sum_ages_future_hypothesis = 21

# the hypothesis refers to the future sum of their ages mentioned in the premise
if sum_ages_future_hypothesis != sum_ages_future_premise:
    # check if the future sum of their ages in the hypothesis contradicts the future sum of their ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

