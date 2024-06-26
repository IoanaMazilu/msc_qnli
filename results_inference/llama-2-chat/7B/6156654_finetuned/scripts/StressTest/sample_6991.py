distance_sita = 12
distance_geeta = 12

# the hypothesis refers to the distance each twin ran, which is also mentioned in the premise
if distance_sita > 52 or distance_geeta > 52:
    # check if the distance in the hypothesis contradicts the premise's distance limit
    label = "contradiction"
elif distance_sita < distance_geeta:
    # check if the distance of Geeta is less than the distance of Sita
    label = "contradiction"
else:
    # if the distances are equal, it is a neutral case
    label = "neutral"

print(label)
