english_marks_premise = 76
math_marks_premise = 65
chem_marks_premise = 82
bio_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
math_marks_hypothesis = 65
chem_marks_hypothesis = 82
bio_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in various subjects mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or math_marks_premise < math_marks_hypothesis or chem_marks_premise < chem_marks_hypothesis or bio_marks_premise < bio_marks_hypothesis or physics_marks_premise < physics_marks_hypothesis:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif english_marks_premise > english_marks_hypothesis and math_marks_premise == math_marks_hypothesis and chem_marks_premise == chem_marks_hypothesis and bio_marks_premise == bio_marks_hypothesis and physics_marks_premise == physics_marks_hypothesis:
    # check if the hypothesis values can be explicitly entailed from the premise ones
    label = "entailment"
else:
    # if the hypothesis values do not contradict or can't be explicitly entailed from the premise ones, we infer neutrality
    label = "neutral"

print(label)
