distance_walked_premise = 31
distance_walked_hypothesis = 81

# the hypothesis talks about the distance walked by Yolanda and Bob, referenced also in the premise
if distance_walked_hypothesis <= distance_walked_premise:
    # check if the hypothesis value contradicts the distance walked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance walked
    # any distance greater than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
