premise_start_point = P
premise_end_point = Q
premise_speed = 90
premise_time_interval = 12
premise_speed_increase = 20

hypothesis_speed = 90
hypothesis_speed_increase = 20

# check if the hypothesis speed is greater than the premise speed
if hypothesis_speed > premise_speed:
    label = "entailment"
# check if the hypothesis speed increase is consistent with the premise speed increase
elif hypothesis_speed_increase == premise_speed_increase:
    label = "neutral"
else:
    label = "contradiction"

print(label)
