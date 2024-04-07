# Premise: Alice leaves City A less than 60 minutes after Bob.
# Hypothesis: Alice leaves City A 30 minutes after Bob.
# Golden Label: neutral

departure_time_difference_premise = 60
departure_time_difference_hypothesis = 30

# the hypothesis talks about the time difference between Alice's and Bob's departures from City A
if departure_time_difference_hypothesis > departure_time_difference_premise:
    # check if the time difference in the hypothesis contradicts the premise (less than 'departure_time_difference_premise')
    label = "contradiction"
elif departure_time_difference_hypothesis < departure_time_difference_premise:
    # if the time difference in the hypothesis is less than in the premise, it can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the time difference in the hypothesis is exactly the same as in the premise, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

