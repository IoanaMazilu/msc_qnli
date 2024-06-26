# Define the variables for the premise
pennies = 100.0
quarters = 783.0
borrowed_quarters = 271.0

# Define the variables for the hypothesis
current_quarters = 513.0

# Calculate the total number of quarters in the premise
total_quarters = pennies / 100 + quarters

# Calculate the number of quarters left after borrowing
remaining_quarters = total_quarters - borrowed_quarters

# Check if the hypothesis value contradicts the premise
if current_quarters!= remaining_quarters:
    label = "contradiction"
else:
    label = "entailment"

print(label)
