# Define the marks Nancy obtained in each subject
nancy_marks_american_literature = 86
nancy_marks_history = 75
nancy_marks_home_economics = 52
nancy_marks_physical_education = 68
nancy_marks_art = 89

# Check if the hypothesis values contradict the premise values
if nancy_marks_american_literature!= 89:
    label = "contradiction"
elif nancy_marks_history!= 75:
    label = "contradiction"
elif nancy_marks_home_economics!= 52:
    label = "contradiction"
elif nancy_marks_physical_education!= 68:
    label = "contradiction"
elif nancy_marks_art!= 89:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
