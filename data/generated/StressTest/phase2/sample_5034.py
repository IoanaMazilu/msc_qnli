# Premise: John has 6 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Hypothesis: John has less than 8 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Golden Label: entailment

friends_premise = 6
friends_hypothesis = 8
car_capacity = 4

# the hypothesis talks about the number of John's friends who want to ride in his car, also mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the number of friends in the premise
    label = "contradiction"
elif friends_premise != friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

