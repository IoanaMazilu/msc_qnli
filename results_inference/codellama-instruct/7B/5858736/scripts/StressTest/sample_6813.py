# Define variables for the premise and hypothesis
num_students_premise = 18
num_students_hypothesis = 48

# Check if the hypothesis value contradicts the premise
if num_students_hypothesis <= num_students_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
