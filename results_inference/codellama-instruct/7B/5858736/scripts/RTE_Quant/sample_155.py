# Define variables for the numerical entities in the premise and hypothesis
num_judges_premise = 8
num_judges_hypothesis = 11

# Extract all quantities as valid numbers
num_judges_premise = int(num_judges_premise)
num_judges_hypothesis = int(num_judges_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_judges_hypothesis > num_judges_premise:
    # The hypothesis talks about a larger number of judges than the premise
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
