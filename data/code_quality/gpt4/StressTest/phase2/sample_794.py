sum_ages_future_premise = 51
sum_ages_future_hypothesis = 61

# the hypothesis refers to the future sum of their ages mentioned in the premise
if sum_ages_future_hypothesis != sum_ages_future_premise:
    # check if the future sum of ages in the hypothesis contradicts the future sum of ages in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are identical
    label = "neutral"

print(label)
