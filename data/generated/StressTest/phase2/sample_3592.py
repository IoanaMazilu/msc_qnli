# Premise: Jose joined him less than 7 months later, investing Rs.
# Hypothesis: Jose joined him 2 months later, investing Rs.
# Golden Label: neutral

months_joined_premise = 7
months_joined_hypothesis = 2

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if months_joined_hypothesis >= months_joined_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'months_joined_premise'
    label = "contradiction"
elif months_joined_hypothesis < months_joined_premise:
    # if the hypothesis value is less than the premise estimate, it does not contradict. But, it also cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)

