premise_marks = [86, 75, 72, 63, 65]
hypothesis_marks = [more than 86, 75, 72, 63, 65]

# the hypothesis refers to the number of marks scored by Adam in an examination
if len(hypothesis_marks)!= len(premise_marks):
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
elif hypothesis_marks[0] <= premise_marks[0]:
    # check if the estimate of 'hypothesis_marks[0]' contradicts the number of marks in the premise
    label = "contradiction"
elif hypothesis_marks[1:]!= premise_marks[1:]:
    # check if the number of marks in the hypothesis contradicts the number of marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
