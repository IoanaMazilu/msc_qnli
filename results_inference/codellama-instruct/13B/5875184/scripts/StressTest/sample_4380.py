premise_distance = 100
premise_time_1 = 1
premise_time_2 = 3
premise_speed_1 = 50
premise_speed_2 = 60

hypothesis_distance = 100
hypothesis_time_1 = 8
hypothesis_time_2 = 3
hypothesis_speed_1 = 50
hypothesis_speed_2 = 60

# calculate the actual distance traveled by Andrew
actual_distance = premise_distance + (premise_time_1 * premise_speed_1) + (premise_time_2 * premise_speed_2)

# calculate the estimated distance traveled by Andrew
estimated_distance = hypothesis_distance + (hypothesis_time_1 * hypothesis_speed_1) + (hypothesis_time_2 * hypothesis_speed_2)

# check if the estimated distance contradicts the actual distance
if estimated_distance < actual_distance:
    label = "contradiction"
elif estimated_distance > actual_distance:
    label = "entailment"
else:
    label = "neutral"

print(label)
