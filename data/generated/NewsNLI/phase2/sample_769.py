# Premise: The sources said the gadget will have a screen between 7 and 8 inches wide, and one said that it will not have the high-definition'' retina display'' screen of the new iPad.
# Hypothesis: Sources tell Bloomberg'' iPad Mini'' would have 7-8 inche screen.
# Golden Label: neutral

# Define the range of screen sizes for the gadget in the premise and hypothesis
screen_size_premise = range(7, 9)
screen_size_hypothesis = range(7, 9)

# If the screen sizes of the gadget in the premise and hypothesis do not overlap, it's a contradiction
if not set(screen_size_hypothesis).intersection(screen_size_premise):
    label = "contradiction"
else:
    # In case the screen sizes overlap, there is no information in the hypothesis that contradicts the premise
    # However, there is also no explicit entailment from the premise as additional details about the gadget's screen are not present in the hypothesis
    label = "neutral"

print(label)
