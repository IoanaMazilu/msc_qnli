english_mark_premise = 70
math_mark_premise = 60
physics_mark_premise = 78
chemistry_mark_premise = 60
biology_mark_premise = 65

english_mark_hypothesis = 60
math_mark_hypothesis = 60
physics_mark_hypothesis = 78
chemistry_mark_hypothesis = 60
biology_mark_hypothesis = 65

# the hypothesis refers to the marks obtained by David in different subjects as mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the 'english_mark_hypothesis' contradicts the marks obtained in English subject in the premise
    label = "contradiction"
elif math_mark_hypothesis >= math_mark_premise:
    # check if the 'math_mark_hypothesis' contradicts the marks obtained in Mathematics subject in the premise
    label = "contradiction"
elif physics_mark_hypothesis > physics_mark_premise:
    # check if the 'physics_mark_hypothesis' contradicts the marks obtained in Physics subject in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the 'chemistry_mark_hypothesis' contradicts the marks obtained in Chemistry subject in the premise
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the 'biology_mark_hypothesis' contradicts the marks obtained in Biology subject in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
