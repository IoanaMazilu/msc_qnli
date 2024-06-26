# Define variables for the premise and hypothesis
white_socks_premise = 0.4
black_socks_premise = 1 - white_socks_premise

# Define variables for the hypothesis
white_socks_hypothesis = 0.8
black_socks_hypothesis = 1 - white_socks_hypothesis

# Check if the hypothesis values contradict the premise
if white_socks_hypothesis > white_socks_premise:
    # The hypothesis value contradicts the premise, so the label is "contradiction"
    label = "contradiction"
elif black_socks_hypothesis > black_socks_premise:
    # The hypothesis value contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
