marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [less_than_86, 65, 82, 67, 85]

# define variables for each mark category
english_mark = marks_premise[0]
mathematics_mark = marks_premise[1]
physics_mark = marks_premise[2]
chemistry_mark = marks_premise[3]
biology_mark = marks_premise[4]

# compare each mark category in the hypothesis with the corresponding mark category in the premise
if english_mark < marks_hypothesis[0]:
    label = "contradiction"
elif mathematics_mark < marks_hypothesis[1]:
    label = "contradiction"
elif physics_mark < marks_hypothesis[2]:
    label = "contradiction"
elif chemistry_mark < marks_hypothesis[3]:
    label = "contradiction"
elif biology_mark < marks_hypothesis[4]:
    label = "contradiction"
else:
    # if no contradiction is found, we can infer entailment
    label = "entailment"

print(label)
