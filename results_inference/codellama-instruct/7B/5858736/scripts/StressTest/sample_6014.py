premise_karen_speed = 60
premise_tom_speed = 45
hypothesis_karen_speed = 20
hypothesis_tom_speed = 45

# calculate the distance that Tom will drive before Karen wins the bet
tom_distance = (premise_karen_speed - hypothesis_karen_speed) * (premise_tom_speed - hypothesis_tom_speed)

# check if the hypothesis values contradict the premise ones
if tom_distance <= 0:
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed of Karen and Tom
    # any number of E miles greater than 'tom_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
