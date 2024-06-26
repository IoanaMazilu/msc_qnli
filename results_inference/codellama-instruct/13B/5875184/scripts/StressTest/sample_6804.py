premise_distance = 31
hypothesis_distance = 81

# the hypothesis refers to the distance traveled by Bob, which is mentioned in the premise
if hypothesis_distance <= premise_distance:
    # check if the estimate of 'hypothesis_distance' contradicts the distance traveled by Yolanda in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Yolanda
    # any distance greater than 'premise_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
