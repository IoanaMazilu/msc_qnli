travel_speed_from_A_to_B = 40
travel_speed_from_B_to_C = 60

# the hypothesis refers to the travel speed from A to B and B to C
if travel_speed_from_A_to_B!= travel_speed_from_B_to_C:
    # check if the speed from A to B and B to C contradicts the hypothesis
    label = "contradiction"
elif travel_speed_from_A_to_B > 50 or travel_speed_from_B_to_C < 60:
    # check if the speed from A to B or B to C contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, it is an entailment
    label = "entailment"

print(label)
