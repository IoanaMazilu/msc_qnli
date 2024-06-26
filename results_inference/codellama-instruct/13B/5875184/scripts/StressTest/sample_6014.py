premise_distance = 100
premise_speed_karen = 60
premise_speed_tom = 45

hypothesis_distance = 100
hypothesis_speed_karen = 20
hypothesis_speed_tom = 45

# calculate the time taken by Karen to drive the premise distance
premise_time_karen = premise_distance / premise_speed_karen

# calculate the time taken by Tom to drive the premise distance
premise_time_tom = premise_distance / premise_speed_tom

# calculate the time taken by Tom to drive the hypothesis distance
hypothesis_time_tom = hypothesis_distance / hypothesis_speed_tom

# calculate the time difference between Karen and Tom
time_difference = premise_time_karen - premise_time_tom

# calculate the distance driven by Tom before Karen wins the bet
distance_before_win = hypothesis_time_tom * hypothesis_speed_tom

# check if the distance driven by Tom before Karen wins the bet is greater than the premise distance
if distance_before_win > premise_distance:
    # if the distance driven by Tom before Karen wins the bet is greater than the premise distance, the hypothesis is entailed
    label = "entailment"
else:
    # if the distance driven by Tom before Karen wins the bet is less than or equal to the premise distance, the hypothesis is not entailed
    label = "neutral"

print(label)
