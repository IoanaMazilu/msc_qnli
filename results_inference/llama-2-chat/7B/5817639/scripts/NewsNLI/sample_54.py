labels = ["entailment", "neutral"]

# Define variables for premise and hypothesis
columbia_letter_premise = 10
oz_faculty_premise = 1

# Define variables for hypothesis
ten_physicians_hypothesis = 10
columbia_letter_hypothesis = 1

# Check if the hypothesis contradicts the premise
if ten_physicians_hypothesis!= columbia_letter_premise:
    label = "contradiction"
else:
    # Check if the hypothesis values do not contradict the premise
    if oz_faculty_hypothesis!= oz_faculty_premise:
        label = "contradiction"
    else:
        label = "entailment"

print(label)
