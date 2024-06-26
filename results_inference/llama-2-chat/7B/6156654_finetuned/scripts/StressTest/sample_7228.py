marks_american_literature = 66
marks_history = 75
marks_home_economics = 52
marks_physical_education = 68
marks_art = 89

# the hypothesis refers to the same marks obtained by Nancy in different subjects
if marks_american_literature!= 75 or marks_history!= 75 or marks_home_economics!= 52 or marks_physical_education!= 68 or marks_art!= 89:
    # check if any of the marks in the hypothesis contradicts the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis marks do not contradict the premise marks, we can infer entailment
    label = "entailment"

print(label)
