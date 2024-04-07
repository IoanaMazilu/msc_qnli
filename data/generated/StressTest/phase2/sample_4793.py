# Premise: Dacid obtained 70, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained less than 70, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

english_mark_premise = 70
math_mark_premise = 63
physics_mark_premise = 80
chemistry_mark_premise = 63
biology_mark_premise = 65

english_mark_hypothesis = 70
math_mark_hypothesis = 63
physics_mark_hypothesis = 80
chemistry_mark_hypothesis = 63
biology_mark_hypothesis = 65

# the hypothesis refers to the same marks obtained by Dacid in different subjects as stated in the premise
if english_mark_hypothesis >= english_mark_premise or math_mark_hypothesis >= math_mark_premise or physics_mark_hypothesis >= physics_mark_premise or chemistry_mark_hypothesis >= chemistry_mark_premise or biology_mark_hypothesis >= biology_mark_premise:
    # check if the hypothesis value contradicts the estimate of less than the marks in the premise
    label = "contradiction"
else:
    # the premise gives the exact marks for the subjects
    # any marks less than the ones in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

