premise_distance = 8
premise_speed = 40
premise_stop_time = 15
premise_additional_distance = 20
premise_additional_speed = 60

hypothesis_distance = 5
hypothesis_speed = 40
hypothesis_stop_time = 15
hypothesis_additional_distance = 20
hypothesis_additional_speed = 60

# calculate the total distance traveled by Jerry in the premise
premise_total_distance = premise_distance + (premise_additional_distance / premise_additional_speed)

# calculate the total distance traveled by Jerry in the hypothesis
hypothesis_total_distance = hypothesis_distance + (hypothesis_additional_distance / hypothesis_additional_speed)

# check if the total distance traveled by Jerry in the hypothesis contradicts the total distance traveled in the premise
if hypothesis_total_distance <= premise_total_distance:
    label = "contradiction"
else:
    label = "neutral"

print(label)