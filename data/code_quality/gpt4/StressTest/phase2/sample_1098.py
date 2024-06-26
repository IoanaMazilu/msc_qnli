friends_premise = 6
friends_hypothesis = 5
car_capacity = 3

# the hypothesis refers to the number of John's friends mentioned in the premise
if friends_hypothesis >= friends_premise:
    # check if the estimate of 'friends_hypothesis' contradicts the number of John's friends in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
