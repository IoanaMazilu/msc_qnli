# Premise: Shekar scored 76, 65, 82, 62 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored 46, 65, 82, 62 and 85 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: contradiction

math_marks_premise = 76
math_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_marks_premise = 82
social_marks_hypothesis = 82
english_marks_premise = 62
english_marks_hypothesis = 62
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis talks about the marks scored by Shekar in various subjects, which are also mentioned in the premise
if math_marks_hypothesis != math_marks_premise:
    # check if the number of mathematics marks in the hypothesis contradicts the number of mathematics marks in the premise
    label = "contradiction"
elif science_marks_hypothesis != science_marks_premise:
    # check if the number of science marks in the hypothesis contradicts the number of science marks in the premise
    label = "contradiction"
elif social_marks_hypothesis != social_marks_premise:
    # check if the number of social studies marks in the hypothesis contradicts the number of social studies marks in the premise
    label = "contradiction"
elif english_marks_hypothesis != english_marks_premise:
    # check if the number of english marks in the hypothesis contradicts the number of english marks in the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if the number of biology marks in the hypothesis contradicts the number of biology marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

