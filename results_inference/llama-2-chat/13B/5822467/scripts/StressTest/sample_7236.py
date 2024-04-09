vacation_distance_premise = 240
vacation_distance_hypothesis = 440

# the hypothesis refers to the distance traveled on the first day of the vacation
if vacation_distance_hypothesis <= vacation_distance_premise:
    # check if the hypothesis value contradicts the estimate of 'vacation_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled less than 'vacation_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
