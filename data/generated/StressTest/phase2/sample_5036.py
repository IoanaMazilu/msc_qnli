# Premise: John has 6 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Hypothesis: John has less than 6 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Golden Label: contradiction

friends_want_ride_premise = 6
friends_want_ride_hypothesis = 6

# The hypothesis refers to the number of John's friends who want to ride in his car, also mentioned in the premise
if friends_want_ride_hypothesis >= friends_want_ride_premise:
    # check if the hypothesis value contradicts the estimate of less than 'friends_want_ride_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

