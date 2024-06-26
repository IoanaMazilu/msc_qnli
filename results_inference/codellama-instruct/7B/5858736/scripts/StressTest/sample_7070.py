# Define variables for the numerical entities in the premise and hypothesis
work_hours_premise = 16
orders_hour_premise = 40
earnings_premise = work_hours_premise * orders_hour_premise

# Define variables for the numerical entities in the hypothesis
work_hours_hypothesis = 18
orders_hour_hypothesis = 40
earnings_hypothesis = work_hours_hypothesis * orders_hour_hypothesis

# Check if the hypothesis values contradict the premise
if earnings_hypothesis <= earnings_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
