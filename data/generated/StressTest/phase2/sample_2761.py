# Premise: The total marks obtained by a student in Mathematics and Physics is less than 70 and his score in Chemistry is 20 marks more than that in Physics.
# Hypothesis: The total marks obtained by a student in Mathematics and Physics is 20 and his score in Chemistry is 20 marks more than that in Physics.
# Golden Label: neutral

total_marks_premise = 70
total_marks_hypothesis = 20
extra_marks_in_chemistry_premise = extra_marks_in_chemistry_hypothesis = 20

# the hypothesis talks about the total marks obtained by a student in Mathematics and Physics 
# and the difference between the scores in Chemistry and Physics, both referenced also in the premise
if total_marks_hypothesis >= total_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_marks_premise'
    label = "contradiction"
elif extra_marks_in_chemistry_hypothesis != extra_marks_in_chemistry_premise:
    # check if the difference in Chemistry and Physics scores in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif total_marks_hypothesis < total_marks_premise and extra_marks_in_chemistry_hypothesis == extra_marks_in_chemistry_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

