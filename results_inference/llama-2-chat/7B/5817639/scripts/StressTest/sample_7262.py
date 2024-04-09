# Define variables for the premise and hypothesis
carol_rectangle_premise = 12
carol_rectangle_hypothesis = 32
jordan_rectangle_premise = 9
jordan_rectangle_hypothesis = 9

# Calculate the width of Jordan's rectangle
jordan_rectangle_width = jordan_rectangle_hypothesis / jordan_rectangle_premise

# Check for entailment, contradiction, or neutrality
if jordan_rectangle_width <= 1:
    # The hypothesis value contradicts the premise value
    label = "contradiction"
elif jordan_rectangle_width > 1:
    # The premise value does not contradict the hypothesis value
    label = "entailment"
else:
    # The hypothesis value does not contradict the premise value, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
