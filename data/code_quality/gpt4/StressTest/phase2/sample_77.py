distance_premise = 12
distance_hypothesis = 12

# the hypothesis refers to the distance between Efrida and Frazer's homes mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance between Efrida and Frazer's homes
    # any distance not equal to 'distance_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
