english_marks_premise = 76
math_marks_premise = 98
physics_marks_premise = 99
chem_marks_premise = 100
bio_marks_premise = 98

english_marks_hypothesis = 96
math_marks_hypothesis = 98
physics_marks_hypothesis = 99
chem_marks_hypothesis = 100
bio_marks_hypothesis = 98

# the hypothesis talks about the marks obtained by Dacid in English, Mathematics, Physics, Chemistry, and Biology
# these marks are also referenced in the premise

if english_marks_hypothesis <= english_marks_premise or math_marks_hypothesis <= math_marks_premise or physics_marks_hypothesis <= physics_marks_premise or chem_marks_hypothesis <= chem_marks_premise or bio_marks_hypothesis <= bio_marks_premise:
    # if the marks obtained by Dacid in any subject in the hypothesis are less than or equal to the marks mentioned in the premise, it is a contradiction
    label = "contradiction"
else:
    # if none of the marks obtained by Dacid in the hypothesis are less than the marks mentioned in the premise, it is neutral
    # because the premise cannot explicitly entail the exact marks mentioned in the hypothesis, but it doesn't contradict them either
    label = "neutral"

print(label)
