english_mark_premise = 76
english_mark_hypothesis = 66
math_mark_premise = 65
math_mark_hypothesis = 65
chemistry_mark_premise = 82
chemistry_mark_hypothesis = 82
biology_mark_premise = 67
biology_mark_hypothesis = 67
physics_mark_premise = 85
physics_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject, as mentioned in the premise
if english_mark_hypothesis <= english_mark_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise or chemistry_mark_hypothesis!= chemistry_mark_premise or biology_mark_hypothesis!= biology_mark_premise or physics_mark_hypothesis!= physics_mark_premise:
    # check if the marks in each subject in the hypothesis contradict the corresponding marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
