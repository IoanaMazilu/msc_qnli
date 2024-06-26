passenger_combinations_premise = 2
friends_number_premise = 4
passenger_combinations_hypothesis = 8
friends_number_hypothesis = 4

# the hypothesis refers to the number of combinations of passengers and friends mentioned in the premise
if friends_number_premise != friends_number_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
elif passenger_combinations_hypothesis <= passenger_combinations_premise:
    # check if the number of passenger combinations in the hypothesis contradicts the number of passenger combinations estimated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
