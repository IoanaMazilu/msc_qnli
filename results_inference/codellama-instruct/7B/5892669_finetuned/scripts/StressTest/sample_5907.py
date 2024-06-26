math_marks_premise = 76
math_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_marks_premise <= math_marks_hypothesis:
    # check if the estimate of'math_marks_hypothesis' contradicts the number of math marks in the premise
    label = "contradiction"
elif science_marks_hypothesis!= science_marks_premise or social_studies_marks_hypothesis!= social_studies_marks_premise or english_marks_hypothesis!= english_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the number of marks in any of the other subjects in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
