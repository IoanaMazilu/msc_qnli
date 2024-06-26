# defining the variables
right_premise = 62
right_hypothesis = 12
left_premise = 4
left_hypothesis = 4

# the hypothesis talks about Rahul's position in a line of boys, referenced also in the premise
if left_hypothesis!= left_premise:
    # check if the left position in the hypothesis contradicts the left position in the premise
    label = "contradiction"
elif right_hypothesis <= right_premise:
    # check if Rahul's right position in the hypothesis contradicts the right position in the premise
    label = "contradiction"
else:
    # Rahul's right position in the hypothesis is greater than the right position in the premise, hence entailment
    label = "entailment"

print(label)
