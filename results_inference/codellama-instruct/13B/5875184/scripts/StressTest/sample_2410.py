distance_premise = 100
distance_hypothesis = 300

# the hypothesis refers to the distance covered by the dogsled teams
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
