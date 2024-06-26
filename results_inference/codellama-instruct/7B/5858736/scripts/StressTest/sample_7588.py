# Define variables for the scores
french_score = 86
geography_score = 75
art_score = 72
design_score = 63
history_score = 65

# Calculate the average mark scored by Adam
adam_average = (french_score + geography_score + art_score + design_score + history_score) / 5

# Check if the hypothesis value contradicts the premise
if adam_average <= 46:
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
