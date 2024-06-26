stations_premise = 16
stations_hypothesis = 36

# The hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also referenced in the premise
if stations_hypothesis != stations_premise:
    # Check if the number of stations in the hypothesis contradicts the number of stations mentioned in the premise
    label = "contradiction"
else:
    # If the number of stations in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
