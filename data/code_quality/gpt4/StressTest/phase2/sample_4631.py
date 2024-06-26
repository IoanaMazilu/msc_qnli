# Defining the marks obtained by Dacid in each subject in the premise and the hypothesis
english_marks_premise = 73
mathematics_marks_premise = 69
physics_marks_premise = 92
chemistry_marks_premise = 64
biology_marks_premise = 82

english_marks_hypothesis = 33
mathematics_marks_hypothesis = 69
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 64
biology_marks_hypothesis = 82

# The hypothesis refers to the marks obtained by Dacid in each subject mentioned in the premise
if english_marks_premise != english_marks_hypothesis:
    # Check if the English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif mathematics_marks_premise != mathematics_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis:
    # Check if the marks in other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
