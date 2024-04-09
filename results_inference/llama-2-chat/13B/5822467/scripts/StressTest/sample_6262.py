# Define variables for the numerical entities in the premise and hypothesis
annie_working_alone_premise = 40
annie_working_alone_hypothesis = 10

# Check if the hypothesis value contradicts the premise estimate
if annie_working_alone_hypothesis < annie_working_alone_premise:
    # The hypothesis value contradicts the premise estimate, so the label is contradiction
    label = "contradiction"
elif annie_working_alone_hypothesis == annie_working_alone_premise:
    # The hypothesis value is equal to the premise estimate, so the label is entailment
    label = "entailment"
else:
    # The hypothesis value is greater than the premise estimate, but not contradictory
    label = "neutral"

print(label)
