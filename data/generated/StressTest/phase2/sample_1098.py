# Premise: John has 6 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Hypothesis: John has more than 5 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Golden Label: entailment

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

