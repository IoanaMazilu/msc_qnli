war_duration_premise = 74
diplomatic_restoration_time_premise = 8*365
diplomatic_restoration_time_hypothesis = 74

# the hypothesis talks about the duration of the war and the time it took to restore full diplomatic relations
# we compare these durations to check for contradiction or entailment
if war_duration_premise != diplomatic_restoration_time_hypothesis:
    # if the duration of the war contradicts the time of restoration mentioned in the hypothesis
    label = "contradiction"
else:
    label = "entailment"

print(label)
