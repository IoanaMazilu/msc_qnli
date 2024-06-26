# Define variables for the numerical entities in the premise and hypothesis
premise_more_than_500 = 500
premise_share_of_greg = 600
hypothesis_more_than_500 = 600
hypothesis_share_of_greg = 600

# Extract all quantities as valid numbers
premise_more_than_500 = int(premise_more_than_500)
premise_share_of_greg = int(premise_share_of_greg)
hypothesis_more_than_500 = int(hypothesis_more_than_500)
hypothesis_share_of_greg = int(hypothesis_share_of_greg)

# Check if the hypothesis values contradict the premise
if hypothesis_more_than_500 < premise_more_than_500:
    label = "contradiction"
elif hypothesis_share_of_greg!= premise_share_of_greg:
    label = "contradiction"
else:
    label = "neutral"

print(label)
