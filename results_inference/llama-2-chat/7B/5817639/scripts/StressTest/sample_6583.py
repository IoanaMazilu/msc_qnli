# Premise: In how many ways can you seat more than 2 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
bench_seats_premise = 2

# Hypothesis: In how many ways can you seat 5 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
bench_seats_hypothesis = 5

# Variables to represent the number of seats on the bench
bench_seats = bench_seats_premise

# Check if the number of seats in the hypothesis contradicts the number of seats in the premise
if bench_seats_hypothesis < bench_seats_premise:
    label = "contradiction"
else:
    # If the number of seats in the hypothesis is greater than or equal to the number of seats in the premise, we can infer entailment
    label = "entailment"

print(label)
