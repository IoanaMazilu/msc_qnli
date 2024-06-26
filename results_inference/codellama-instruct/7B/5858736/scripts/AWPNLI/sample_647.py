people_watching_premise = 532.0
seats_free_premise = 750.0
seats_hypothesis = 1284.0

# the hypothesis refers to the number of seats, which are also mentioned in the premise
# compute the total number of seats in the premise
total_seats_premise = people_watching_premise * seats_free_premise
if seats_hypothesis!= total_seats_premise:
    # check if the number of seats in the hypothesis contradicts the number of seats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
