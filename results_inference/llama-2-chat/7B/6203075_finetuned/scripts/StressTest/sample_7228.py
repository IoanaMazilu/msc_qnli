# defining the marks obtained by Nancy in each subject
marks_american_lit = 66
marks_history = 75
marks_home_ec = 52
marks_phys_ed = 68
marks_art = 89

# defining the total marks obtained by Nancy
total_marks = marks_american_lit + marks_history + marks_home_ec + marks_phys_ed + marks_art

# comparing the total marks obtained by Nancy in the premise and hypothesis
if total_marks <= 86 and total_marks <= 75 and total_marks <= 52 and total_marks <= 68 and total_marks <= 89:
    # if the total marks obtained by Nancy in the hypothesis is consistent with the premise
    label = "entailment"
else:
    # if the total marks obtained by Nancy in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
