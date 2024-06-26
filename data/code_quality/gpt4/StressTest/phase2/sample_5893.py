distance_delhi_mathura_premise = 310
distance_delhi_mathura_hypothesis = 110

# the hypothesis specifies the exact distance between Delhi and Mathura
if distance_delhi_mathura_hypothesis >= distance_delhi_mathura_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_delhi_mathura_premise' kms
    label = "contradiction"
else:
    # the premise gives only an upper limit for the distance
    # any distance less than 'distance_delhi_mathura_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
