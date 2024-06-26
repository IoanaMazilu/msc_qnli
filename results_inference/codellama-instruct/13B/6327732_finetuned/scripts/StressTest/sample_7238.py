distance_traveled_premise = 240
distance_traveled_hypothesis = 340

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance greater than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
