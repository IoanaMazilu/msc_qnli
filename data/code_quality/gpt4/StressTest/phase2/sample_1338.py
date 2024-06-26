english_marks_premise = 76
math_marks_premise = 65
physics_marks_premise = 82
chem_marks_premise = 67
bio_marks_premise = 85

english_marks_hypothesis = 46
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chem_marks_hypothesis = 67
bio_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in various subjects, mentioned in the premise
if english_marks_premise <= english_marks_hypothesis:
    # check if the estimate of 'english_marks_hypothesis' contradicts the English marks in the premise
    label = "contradiction"
elif math_marks_premise < math_marks_hypothesis or physics_marks_premise < physics_marks_hypothesis or chem_marks_premise < chem_marks_hypothesis or bio_marks_premise < bio_marks_hypothesis:
    # check if the marks in any of the other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
