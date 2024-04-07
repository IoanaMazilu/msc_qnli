# Premise: Alice leaves City A 30 minutes after Bob.
# Hypothesis: Alice leaves City A less than 70 minutes after Bob.
# Golden Label: entailment

leave_after_bob_premise = 30
leave_after_bob_hypothesis = 70

# the hypothesis refers to the time Alice leaves City A after Bob, same as the premise
if leave_after_bob_hypothesis < leave_after_bob_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
elif leave_after_bob_hypothesis == leave_after_bob_premise:
    # check if the hypothesis time is exactly the same as the premise time
    label = "entailment"
else:
    # if the hypothesis time is greater than the premise time, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

