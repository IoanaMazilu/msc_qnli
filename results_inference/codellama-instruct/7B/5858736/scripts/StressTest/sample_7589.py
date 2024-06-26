# Define variables for the scores and the total marks
french_score = 86
geography_score = 75
art_score = 72
history_score = 63
physical_education_score = 65
total_marks = 100

# Calculate the average mark scored by Adam
adam_average_mark = (french_score + geography_score + art_score + history_score + physical_education_score) / total_marks

# Check if the hypothesis is entailed from the premise
if adam_average_mark > 86:
    label = "entailment"
else:
    label = "contradiction"

print(label)
