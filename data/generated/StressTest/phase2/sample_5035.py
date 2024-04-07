# Premise: John has less than 8 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Hypothesis: John has 6 friends who want to ride in his new car that can accommodate only 4 people at a time (John plus 3 passengers)
# Golden Label: neutral

friends_premise = 8
friends_hypothesis = 6
car_capacity = 4

# the hypothesis talks about the number of John's friends who want to ride in his car, referenced also in the premise
if friends_hypothesis >= friends_premise:
    # check if the hypothesis value contradicts the estimate of less than 'friends_premise'
    label = "contradiction"
elif car_capacity != 4:
    # check if the car's capacity in the hypothesis contradicts the car's capacity reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of John's friends
    # any number of friends less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

