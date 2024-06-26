# Define variables with representative names for the numerical entities in both inputs
coloring_books_premise = 48.0
gave_away_premise = 34.0 + 3.0
left_hypothesis = 12.0

# Extract all quantities as valid numbers (integers or floats)
coloring_books_premise = float(coloring_books_premise)
gave_away_premise = float(gave_away_premise)
left_hypothesis = float(left_hypothesis)

# Comments explaining the comparison
# The hypothesis states that Faye would have 12 coloring books left
# The premise states that Faye gave away 34 coloring books and then gave away 3 more

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Use the correct comparison operators
if left_hypothesis < gave_away_premise:
    # Check if the number of left coloring books contradicts the number of gave-away coloring books
    label = "contradiction"
elif left_hypothesis > gave_away_premise:
    # Check if the number of left coloring books entails the number of gave-away coloring books
    label = "entailment"
else:
    # If the number of left coloring books and the number of gave-away coloring books are equal, there is no contradiction or entailment
    label = "neutral"

print(label)
