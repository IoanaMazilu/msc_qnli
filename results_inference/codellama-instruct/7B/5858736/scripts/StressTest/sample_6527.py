# Define variables for the numerical entities in the premise and hypothesis
num_flights_premise = 3
num_flights_hypothesis = 2

# Extract the quantities as valid numbers
num_flights_premise = int(num_flights_premise)
num_flights_hypothesis = int(num_flights_hypothesis)

# Perform calculations
on_time_rate_premise = (num_flights_premise / 3) * 100
on_time_rate_hypothesis = (num_flights_hypothesis / 3) * 100

# Check if the hypothesis value contradicts the premise
if on_time_rate_hypothesis <= on_time_rate_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
