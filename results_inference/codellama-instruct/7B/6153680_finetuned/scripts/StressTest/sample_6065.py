marks_english = 86
marks_mathematics = 89
marks_physics = 82
marks_chemistry = 87
marks_biology = 81

# the hypothesis refers to the same marks obtained by Dacid in the same subjects
# the hypothesis values are the same as the premise values
if marks_english == 86 and marks_mathematics == 89 and marks_physics == 82 and marks_chemistry == 87 and marks_biology == 81:
    label = "entailment"
else:
    label = "contradiction"

print(label)
