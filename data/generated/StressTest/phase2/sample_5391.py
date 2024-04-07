# Premise: Alice drives at a constant speed of 30 km per hour.
# Hypothesis: Alice drives at a constant speed of less than 40 km per hour.
# Golden Label: entailment

alice_speed_premise = 30
alice_speed_hypothesis = 40

# the hypothesis refers to Alice's driving speed mentioned in the premise
if alice_speed_premise >= alice_speed_hypothesis:
    # check if the speed of 'alice_speed_premise' contradicts the speed limit in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
