# Define the variables
trumpet_cost = 145.16
song_book_cost = 5.84
total_spent = trumpet_cost + song_book_cost

# Calculate the net amount that Mike spent
net_amount = total_spent - trumpet_cost

# Check if the hypothesis values contradict the premise values
if net_amount!= 134.7:
    label = "contradiction"
else:
    label = "entailment"

print(label)
