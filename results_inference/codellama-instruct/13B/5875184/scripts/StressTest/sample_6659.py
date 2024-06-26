premise_speed_karen = 60
premise_speed_tom = 45
hypothesis_speed_karen = 70
hypothesis_speed_tom = 45

# calculate the total distance driven by Karen and Tom
premise_distance = premise_speed_karen * premise_speed_tom
hypothesis_distance = hypothesis_speed_karen * hypothesis_speed_tom

# check if the distance driven by Tom is greater than the distance driven by Karen
if hypothesis_distance > premise_distance:
    # if the distance driven by Tom is greater than the distance driven by Karen, then Karen will win the bet
    label = "entailment"
else:
    # if the distance driven by Tom is not greater than the distance driven by Karen, then the bet cannot be entailed
    label = "neutral"

print(label)
