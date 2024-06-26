distance_traveled_premise = 300
distance_traveled_hypothesis = 200

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation
if distance_traveled_hypothesis >= distance_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled less than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
