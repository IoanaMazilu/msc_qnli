english_premise = 86
math_premise = 85
physics_premise = 92
chemistry_premise = 87
biology_premise = 95

english_hypothesis = 86
math_hypothesis = 85
physics_hypothesis = 92
chemistry_hypothesis = 87
biology_hypothesis = 95

# The hypothesis refers to the marks obtained by Dacid in five subjects mentioned in the premise
if english_hypothesis >= english_premise or math_hypothesis >= math_premise or physics_hypothesis >= physics_premise or chemistry_hypothesis >= chemistry_premise or biology_hypothesis >= biology_premise:
    # If any of the marks in the hypothesis is not less than the corresponding mark in the premise, it contradicts the hypothesis
    label = "contradiction"
else:
    # If all the marks in the hypothesis are less than the corresponding marks in the premise, it supports the hypothesis
    label = "entailment"

print(label)
