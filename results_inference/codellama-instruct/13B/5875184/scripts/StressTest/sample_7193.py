premise = "Similarly, there's a train that leaves Chennai bound for Jammu on everyday of the week exactly at 12 noon."
hypothesis = "Similarly, there's a train that leaves Chennai bound for Jammu on everyday of the week exactly at less than 12 noon."

# extract the time from the premise
premise_time = premise.split("at")[1].strip()

# extract the time from the hypothesis
hypothesis_time = hypothesis.split("at")[1].strip()

# compare the times
if premise_time == hypothesis_time:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif premise_time < hypothesis_time:
    # the hypothesis is consistent with the premise
    label = "entailment"
else:
    # the hypothesis is not consistent with the premise
    label = "neutral"

print(label)
