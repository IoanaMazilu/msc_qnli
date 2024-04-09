people_premise = 532.0
seats_premise = 750.0
seats_hypothesis = 1284.0

# compute the total number of seats in the premise
total_seats_premise = seats_premise + people_premise

if seats_hypothesis > total_seats_premise:
    # check if the number of seats in the hypothesis contradicts the number of seats from the premise
    label = "contradiction"
elif seats_hypothesis < total_seats_premise:
    # check if the number of seats in the hypothesis is less than the total number of seats in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
