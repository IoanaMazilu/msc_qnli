distance_sita = 12
distance_geeta = 12
total_distance = distance_sita + distance_geeta

# the hypothesis talks about the distance each twin ran, which is also mentioned in the premise
if total_distance > 52:
    # check if the total distance is greater than 52 km, which is the hypothesis value
    label = "entailment"
elif total_distance < 52:
    # check if the total distance is less than 52 km, which is the hypothesis value
    label = "contradiction"
else:
    # if the total distance is equal to 52 km, then it is neutral
    label = "neutral"

print(label)
