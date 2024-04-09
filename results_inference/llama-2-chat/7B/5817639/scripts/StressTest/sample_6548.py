distance_premise = 15
distance_hypothesis = float(16)

# the hypothesis talks about a greater distance between West-Town and East-Town than the premise reports
if distance_hypothesis > distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the premise provides a single estimate for the distance, and the hypothesis can be entailed from that estimate
    label = "entailment"

print(label)
