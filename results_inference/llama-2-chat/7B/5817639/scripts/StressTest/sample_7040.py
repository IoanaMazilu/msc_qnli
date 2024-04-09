# Define variables for the premise and hypothesis
premise_marks_geography = 56
premise_marks_history = 60
premise_marks_government = 72
premise_marks_art = 80
premise_marks_computer_science = 85
premise_marks_modern_literature = 80

hypothesis_marks_geography = 56
hypothesis_marks_history = 60
hypothesis_marks_government = 72
hypothesis_marks_art = 80
hypothesis_marks_computer_science = 85
hypothesis_marks_modern_literature = 80

# Check if the hypothesis contradicts the premise
if hypothesis_marks_geography > premise_marks_geography or \
   hypothesis_marks_history > premise_marks_history or \
   hypothesis_marks_government > premise_marks_government or \
   hypothesis_marks_art > premise_marks_art or \
   hypothesis_marks_computer_science > premise_marks_computer_science or \
   hypothesis_marks_modern_literature > premise_marks_modern_literature:
    label = "contradiction"
else:
    # Check if the hypothesis values are consistent with the premise values
    label = "entailment"

print(label)
