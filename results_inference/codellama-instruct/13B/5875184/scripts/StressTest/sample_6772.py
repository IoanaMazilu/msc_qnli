premise_speed_a_b = 50
premise_speed_b_c = 60
hypothesis_speed_a_b = 40
hypothesis_speed_b_c = 60

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C
if hypothesis_speed_a_b > premise_speed_a_b:
    # check if the hypothesis value contradicts the estimate of less than 'premise_speed_a_b'
    label = "contradiction"
elif hypothesis_speed_b_c!= premise_speed_b_c:
    # check if the hypothesis value contradicts the estimate of 'premise_speed_b_c'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of travel
    # any speed greater than 'premise_speed_a_b' and equal to 'premise_speed_b_c' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
