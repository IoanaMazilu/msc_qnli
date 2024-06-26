# extract the numerical entities from the premise and hypothesis
premise_distance = 81
hypothesis_distance = 31

# check if the hypothesis distance is less than the premise distance
if hypothesis_distance < premise_distance:
    # the hypothesis distance is less than the premise distance, so it contradicts the premise
    label = "contradiction"
else:
    # the hypothesis distance is greater than or equal to the premise distance, so it does not contradict the premise
    label = "neutral"

print(label)
