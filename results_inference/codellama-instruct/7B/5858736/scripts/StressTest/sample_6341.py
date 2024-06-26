# Define variables for the numerical entities in the premise and hypothesis
work_hours_premise = 4
work_hours_hypothesis = 4
orders_hour_premise = 40
orders_hour_hypothesis = 40

# Extract all quantities as valid numbers
work_hours_premise = int(work_hours_premise)
work_hours_hypothesis = int(work_hours_hypothesis)
orders_hour_premise = float(orders_hour_premise)
orders_hour_hypothesis = float(orders_hour_hypothesis)

# Calculate the total earnings for the premise
total_earnings_premise = work_hours_premise * orders_hour_premise

# Calculate the total earnings for the hypothesis
total_earnings_hypothesis = work_hours_hypothesis * orders_hour_hypothesis

# Compare the total earnings for the premise and hypothesis
if total_earnings_hypothesis <= total_earnings_premise:
    # The hypothesis value contradicts the total earnings in the premise
    label = "contradiction"
else:
    # The hypothesis value does not contradict the total earnings in the premise
    # Any number of hours greater than 4 hours and an average of $40 per hour is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
