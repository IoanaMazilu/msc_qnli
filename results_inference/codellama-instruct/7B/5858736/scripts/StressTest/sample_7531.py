# Define variables for the premise and hypothesis
premise_list = ["ABC", "BCA", "CAB"]
hypothesis_list = ["ABC", "BCA", "CAB"]

# Extract the number of positive integers in each list
premise_positive_integers = len(premise_list)
hypothesis_positive_integers = len(hypothesis_list)

# Check if the hypothesis contradicts the premise
if hypothesis_positive_integers > premise_positive_integers:
    label = "contradiction"
elif hypothesis_positive_integers < premise_positive_integers:
    label = "neutral"
else:
    label = "entailment"

print(label)
