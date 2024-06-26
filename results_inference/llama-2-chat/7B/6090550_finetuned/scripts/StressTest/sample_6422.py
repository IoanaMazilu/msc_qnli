english_marks_premise = 76
maths_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
maths_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by Arun in different subjects
# we can't infer entailment or contradiction based on the hypothesis, since it does not provide any information about the marks obtained in the other subjects
# the hypothesis values are the same as the premise values for some subjects, but not for others

label = "neutral"

print(label)
