# Define variables with representative names for the numerical entities in both inputs
marks_english_premise = 46
marks_mathematics_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85
marks_total_premise = 46 + 65 + 82 + 67 + 85

marks_english_hypothesis = 76
marks_mathematics_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85
marks_total_hypothesis = 76 + 65 + 82 + 67 + 85

# Extract all quantities as valid numbers (integers or floats)
marks_english_premise = float(marks_english_premise)
marks_mathematics_premise = float(marks_mathematics_premise)
marks_chemistry_premise = float(marks_chemistry_premise)
marks_biology_premise = float(marks_biology_premise)
marks_physics_premise = float(marks_physics_premise)
marks_total_premise = float(marks_total_premise)

marks_english_hypothesis = float(marks_english_hypothesis)
marks_mathematics_hypothesis = float(marks_mathematics_hypothesis)
marks_chemistry_hypothesis = float(marks_chemistry_hypothesis)
marks_biology_hypothesis = float(marks_biology_hypothesis)
marks_physics_hypothesis = float(marks_physics_hypothesis)
marks_total_hypothesis = float(marks_total_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if marks_total_hypothesis <= marks_total_premise:
    # Check if the estimate of'marks_total_hypothesis' contradicts the total marks obtained in the premise
    label = "contradiction"
elif marks_english_hypothesis!= marks_english_premise:
    # Check if the number of marks obtained in English in the hypothesis contradicts the number of marks obtained in English in the premise
    label = "contradiction"
elif marks_mathematics_hypothesis!= marks_mathematics_premise:
    # Check if the number of marks obtained in Mathematics in the hypothesis contradicts the number of marks obtained in Mathematics in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis!= marks_chemistry_premise:
    # Check if the number of marks obtained in Chemistry in the hypothesis contradicts the number of marks obtained in Chemistry in the premise
    label = "contradiction"
elif marks_biology_hypothesis!= marks_biology_premise:
    # Check if the number of marks obtained in Biology in the hypothesis contradicts the number of marks obtained in Biology in the premise
    label = "contradiction"
elif marks_physics_hypothesis!= marks_physics_premise:
    # Check if the number of marks obtained in Physics in the hypothesis contradicts the number of marks obtained in Physics in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
