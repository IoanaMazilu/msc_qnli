# Define variables for the numerical entities in the premise and hypothesis
num_parts_premise_4 = 4
num_parts_premise_6 = 6
num_parts_premise_9 = 9
num_parts_hypothesis_5 = 5
num_parts_hypothesis_6 = 6
num_parts_hypothesis_9 = 9

# Extract all quantities as valid numbers
num_parts_premise_4 = int(num_parts_premise_4)
num_parts_premise_6 = int(num_parts_premise_6)
num_parts_premise_9 = int(num_parts_premise_9)
num_parts_hypothesis_5 = int(num_parts_hypothesis_5)
num_parts_hypothesis_6 = int(num_parts_hypothesis_6)
num_parts_hypothesis_9 = int(num_parts_hypothesis_9)

# Check if the hypothesis values and estimates do not contradict the premise ones
if num_parts_hypothesis_5 <= num_parts_premise_4 and num_parts_hypothesis_6 <= num_parts_premise_6:
    label = "entailment"
elif num_parts_hypothesis_9 > num_parts_premise_9:
    label = "contradiction"
else:
    label = "neutral"

print(label)
