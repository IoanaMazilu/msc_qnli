premise_speed_A_to_B = 30
premise_speed_B_to_C = 60
hypothesis_speed_A_to_B = 40
hypothesis_speed_B_to_C = 60

# the hypothesis talks about the speed of Murali's travel from A to B and from B to C
if hypothesis_speed_A_to_B <= premise_speed_A_to_B:
    # check if the hypothesis value contradicts the estimate of more than 'premise_speed_A_to_B'
    label = "contradiction"
elif hypothesis_speed_B_to_C <= premise_speed_B_to_C:
    # check if the hypothesis value contradicts the estimate of more than 'premise_speed_B_to_C'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
