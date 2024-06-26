distance_delhi_mathura_premise = 410
distance_delhi_mathura_hypothesis = 110

# Hypothesis talks about the distance between Delhi and Mathura which is also referenced in the premise
if distance_delhi_mathura_hypothesis >= distance_delhi_mathura_premise:
    # If the hypothesis distance is greater than or equals the premise distance, this contradicts the 'less than' condition in the premise
    label = "contradiction"
else:
    # The premise gives an upper limit for the distance
    # Any distance less than 'distance_delhi_mathura_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
