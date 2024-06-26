friends_premise = 6
friends_hypothesis = 5
passengers_premise = 4
passengers_hypothesis = 4

# the hypothesis refers to the number of friends who want to ride in the car, which is also mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the number of friends in the premise
    label = "contradiction"
elif passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
