# Premise: Shekar scored 76, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored more than 46, 65, 82, 67 and 75 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: entailment

math_marks_premise = 76
science_marks_premise = 65
social_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 46
science_marks_hypothesis = 65
social_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored in each subject mentioned in the premise
if math_marks_premise <= math_marks_hypothesis or science_marks_premise <= science_marks_hypothesis or social_marks_premise <= social_marks_hypothesis or english_marks_premise <= english_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    # check if the hypothesis estimate contradicts the marks scored in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

