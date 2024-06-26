# Define variables for the premise
cards_before_torn = 33.0
cards_torn = 6.0
cards_received = 23.0

# Define variables for the hypothesis
total_cards = 56.0

# Calculate the total number of cards before and after the torn ones
cards_after_torn = cards_before_torn - cards_torn
cards_total = cards_after_torn + cards_received

# Check if the hypothesis values match the calculated values
if cards_total!= total_cards:
    # If the hypothesis values do not match the calculated values, then the hypothesis is a contradiction
    label = "contradiction"
else:
    # If the hypothesis values match the calculated values, then the hypothesis is entailed
    label = "entailment"

print(label)
