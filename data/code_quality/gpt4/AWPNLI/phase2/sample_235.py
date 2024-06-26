people_watching_premise = 532.0
total_seats_premise = 750.0
empty_seats_hypothesis = 219.0

# the hypothesis refers to the number of empty seats, which can be inferred from the premise
# compute the number of empty seats in the premise
empty_seats_premise = total_seats_premise - people_watching_premise
if empty_seats_hypothesis != empty_seats_premise:
    # check if the number of empty seats in the hypothesis contradicts the number of empty seats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
