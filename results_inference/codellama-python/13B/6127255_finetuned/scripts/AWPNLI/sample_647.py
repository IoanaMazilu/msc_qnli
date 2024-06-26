people_watching_premise = 532.0
free_seats_premise = 750.0
total_seats_hypothesis = 1284.0

# the hypothesis refers to the total number of seats, which can be inferred from the premise
# compute the total number of seats in the premise
total_seats_premise = people_watching_premise + free_seats_premise
if total_seats_hypothesis!= total_seats_premise:
    # check if the total number of seats in the hypothesis contradicts the total number of seats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
