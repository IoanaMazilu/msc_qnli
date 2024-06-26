# Define variables for the premise and hypothesis
male_count_premise = 2
female_count_premise = 3
male_count_hypothesis = 4
female_count_hypothesis = 3

# Check if the hypothesis value contradicts the premise value
if male_count_hypothesis <= male_count_premise:
    label = "contradiction"
else:
    # The premise value only provides an estimate for the number of males,
    # so any number of males greater than the premise value is consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

# Print the label
print(label)
