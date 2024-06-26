premise_distance = 100
premise_time_1 = 1
premise_speed_1 = 44
premise_time_2 = 3
premise_speed_2 = 60

hypothesis_distance = 100
hypothesis_time_1 = 0.5
hypothesis_speed_1 = 44
hypothesis_time_2 = 3
hypothesis_speed_2 = 60

# calculate the total time and distance for both the premise and hypothesis
premise_total_time = premise_time_1 + premise_time_2
premise_total_distance = premise_distance / premise_total_time

hypothesis_total_time = hypothesis_time_1 + hypothesis_time_2
hypothesis_total_distance = hypothesis_distance / hypothesis_total_time

# compare the total distance and time for both the premise and hypothesis
if premise_total_distance > hypothesis_total_distance:
    label = "contradiction"
elif premise_total_time > hypothesis_total_time:
    label = "contradiction"
else:
    label = "neutral"

print(label)
