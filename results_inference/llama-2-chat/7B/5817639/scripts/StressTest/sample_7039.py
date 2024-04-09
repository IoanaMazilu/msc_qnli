# Define variables for the premise and hypothesis
premise_marks_geography = 26
premise_marks_history = 60
premise_marks_government = 72
premise_marks_art = 85
premise_marks_computer_science = 80
premise_marks_modern_literature = 85

hypothesis_marks_geography = 56
hypothesis_marks_history = 60
hypothesis_marks_government = 72
hypothesis_marks_art = 85
hypothesis_marks_computer_science = 80
hypothesis_marks_modern_literature = 85

# Check if the hypothesis marks in each subject contradict the premise marks
if hypothesis_marks_geography <= premise_marks_geography:
    label = "contradiction"
elif hypothesis_marks_history <= premise_marks_history:
    label = "contradiction"
elif hypothesis_marks_government <= premise_marks_government:
    label = "contradiction"
elif hypothesis_marks_art <= premise_marks_art:
    label = "contradiction"
elif hypothesis_marks_computer_science <= premise_marks_computer_science:
    label = "contradiction"
elif hypothesis_marks_modern_literature <= premise_marks_modern_literature:
    label = "contradiction"
else:
    # If no contradiction is found, we can infer entailment
    label = "entailment"

print(label)
