# Define variables for the numerical entities in the premise and hypothesis
num_flights_premise = 3
num_subsequent_flights_premise = 10
on_time_rate_premise = 0.7

num_flights_hypothesis = 3
num_subsequent_flights_hypothesis = 15
on_time_rate_hypothesis = 0.5

# Check if the hypothesis values contradict the premise
if num_subsequent_flights_hypothesis <= num_subsequent_flights_premise:
    # The hypothesis value contradicts the number of subsequent flights mentioned in the premise
    label = "contradiction"
elif on_time_rate_hypothesis <= on_time_rate_premise:
    # The hypothesis value contradicts the on-time departure rate mentioned in the premise
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
