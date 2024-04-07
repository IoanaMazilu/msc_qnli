# Premise: If, five years from now, the sum G of their ages will be less than 71, how old is Stephanie?
# Hypothesis: If, five years from now, the sum G of their ages will be 51, how old is Stephanie?
# Golden Label: neutral

sum_ages_future_premise = 71
sum_ages_future_hypothesis = 51

# The hypothesis refers to the future sum of their ages, which is also mentioned in the premise
if sum_ages_future_hypothesis >= sum_ages_future_premise:
    # Check if the future sum of their ages in the hypothesis contradicts the estimate of less than 'sum_ages_future_premise'
    label = "contradiction"
elif sum_ages_future_hypothesis < sum_ages_future_premise:
    # If the hypothesis value is less than the premise value, it does not contradict the premise
    # However, we cannot explicitly entail the exact age of Stephanie from the premise
    label = "neutral"

print(label)

