math_marks_premise = 76
math_marks_hypothesis = float(input("Enter the number of math marks scored by Shekar: "))

sci_marks_premise = 65
sci_marks_hypothesis = float(input("Enter the number of science marks scored by Shekar: "))

social_marks_premise = 82
social_marks_hypothesis = float(input("Enter the number of social studies marks scored by Shekar: "))

english_marks_premise = 67
english_marks_hypothesis = float(input("Enter the number of English marks scored by Shekar: "))

biology_marks_premise = 75
biology_marks_hypothesis = float(input("Enter the number of biology marks scored by Shekar: "))

# check if the hypothesis values contradict the premise values
if math_marks_hypothesis < math_marks_premise:
    label = "contradiction"
elif sci_marks_hypothesis < sci_marks_premise:
    label = "contradiction"
elif social_marks_hypothesis < social_marks_premise:
    label = "contradiction"
elif english_marks_hypothesis < english_marks_premise:
    label = "contradiction"
elif biology_marks_hypothesis < biology_marks_premise:
    label = "contradiction"
else:
    # if the hypothesis values are consistent with the premise values, we can infer entailment
    label = "entailment"

print(label)
