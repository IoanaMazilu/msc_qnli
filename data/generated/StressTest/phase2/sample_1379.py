# Premise: If Bob runs at a constant rate of 8 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Hypothesis: If Bob runs at a constant rate of less than 8 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Golden Label: contradiction

running_rate_premise = 8
running_rate_hypothesis = 8
total_time = 50

# both the premise and hypothesis refer to Bob's running rate
if running_rate_hypothesis >= running_rate_premise:
    # check if the hypothesis running rate contradicts the premise running rate
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same situation, but with different running rates
    # we cannot explicitly entail the hypothesis from the premise, but the hypothesis does not contradict the premise either
    label = "neutral"

print(label)

