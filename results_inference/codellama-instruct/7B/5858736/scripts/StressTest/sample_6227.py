# Define variables for the premise and hypothesis
num_boys_premise = 300
num_girls_premise = 240
num_boys_hypothesis = 300
num_girls_hypothesis = 240

# Check if the hypothesis values contradict the premise
if num_boys_hypothesis > num_boys_premise or num_girls_hypothesis > num_girls_premise:
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
