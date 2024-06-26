y_premise = 85
distance_premise = 15

# the hypothesis talks about the distance between West-Town and East-Town, which is also mentioned in the premise
if distance_premise >= y_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
