premise_marks = [46, 65, 82, 67, 75]
hypothesis_marks = [76, 65, 82, 67, 75]

# the hypothesis refers to the exact marks scored by Shekar in each subject
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif hypothesis_marks[0] > premise_marks[0]:
    # check if the hypothesis value for Mathematics contradicts the premise one
    label = "contradiction"
elif hypothesis_marks[1]!= premise_marks[1]:
    # check if the hypothesis value for Science contradicts the premise one
    label = "contradiction"
elif hypothesis_marks[2]!= premise_marks[2]:
    # check if the hypothesis value for Social studies contradicts the premise one
    label = "contradiction"
elif hypothesis_marks[3]!= premise_marks[3]:
    # check if the hypothesis value for English contradicts the premise one
    label = "contradiction"
elif hypothesis_marks[4]!= premise_marks[4]:
    # check if the hypothesis value for Biology contradicts the premise one
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
