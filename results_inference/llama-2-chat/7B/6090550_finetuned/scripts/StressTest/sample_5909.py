math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in different subjects, as mentioned in the premise
if math_marks_premise <= math_marks_hypothesis or science_marks_premise <= science_marks_hypothesis or social_studies_marks_premise <= social_studies_marks_hypothesis or english_marks_premise <= english_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    # check if the hypothesis value contradicts the premise values for any of the subjects
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
