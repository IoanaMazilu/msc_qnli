# The hypothesis refers to the floor number and the elevator speed mentioned in the premise
# The hypothesis states that Stalin gets on the elevator at a floor less than 31th floor
# The premise states that Stalin gets on the elevator at the 11th floor

if 11 > 31:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
else:
    # if the floor number in the hypothesis does not contradict the floor number in the premise, we can infer entailment
    label = "entailment"

print(label)
