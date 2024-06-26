# Define variables for the numerical entities in the premise and hypothesis
num_flights_premise = 3
num_subsequent_flights_premise = 10
on_time_rate_premise = 0.7

num_flights_hypothesis = 3
num_subsequent_flights_hypothesis = 15
on_time_rate_hypothesis = 0.8

# Check if the hypothesis values contradict the premise
if num_subsequent_flights_hypothesis <= num_subsequent_flights_premise:
    label = "contradiction"
elif on_time_rate_hypothesis <= on_time_rate_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
