# Premise: Argentina and Britain announced an agreement Thursday to restore full diplomatic ties nearly eight years after they fought a 74 day war over the Falkland Islands a sparsely populated archipelago off Argentina coast in the South Atlantic Ocean.
# Hypothesis: Full diplomatic relations between Argentina and Britain were re-established after 74 days.
# Golden Label: neutral

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

