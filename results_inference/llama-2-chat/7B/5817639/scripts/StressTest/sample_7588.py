# Premise:
premise_marks_french = 46
premise_marks_geography = 75
premise_marks_art_design = 72
premise_marks_history = 63
premise_marks_phys_ed = 65

# Hypothesis:
hypothesis_marks_french = 86
hypothesis_marks_geography = 75
hypothesis_marks_art_design = 72
hypothesis_marks_history = 63
hypothesis_marks_phys_ed = 65

# Variables for comparison
french_marks_premise = premise_marks_french
geography_marks_premise = premise_marks_geography
art_design_marks_premise = premise_marks_art_design
history_marks_premise = premise_marks_history
phys_ed_marks_premise = premise_marks_phys_ed

# Comparison
if hypothesis_marks_french >= french_marks_premise:
    label = "entailment"
elif hypothesis_marks_geography >= geography_marks_premise:
    label = "entailment"
elif hypothesis_marks_art_design >= art_design_marks_premise:
    label = "entailment"
elif hypothesis_marks_history >= history_marks_premise:
    label = "entailment"
elif hypothesis_marks_phys_ed >= phys_ed_marks_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
