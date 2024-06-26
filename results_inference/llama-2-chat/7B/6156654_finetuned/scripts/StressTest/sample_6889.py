# The premise and hypothesis are asking for different numbers of people to be seated on a bench.
# The premise does not mention Rohit's preference, so it cannot be entailed by the hypothesis.
# Therefore, the relation between the premise and hypothesis is neutral.

seats_premise = 8
seats_hypothesis = 6

if seats_premise <= seats_hypothesis:
    # If the number of seats in the premise is less than or equal to the number of seats in the hypothesis,
    # then the hypothesis cannot be entailed from the premise.
    label = "neutral"
else:
    # If the number of seats in the premise is greater than the number of seats in the hypothesis,
    # then the hypothesis can be entailed from the premise.
    label = "contradiction"

print(label)
