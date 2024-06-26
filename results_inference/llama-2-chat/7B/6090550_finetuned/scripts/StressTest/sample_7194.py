scientific_hypothesis = 6.0

# the hypothesis talks about the time required for a train to cover the distance between Chennai and Jammu
# the premise specifies the exact time required for the same distance
if scientific_hypothesis >= 7.0:
    # check if the hypothesis value contradicts the exact time in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

