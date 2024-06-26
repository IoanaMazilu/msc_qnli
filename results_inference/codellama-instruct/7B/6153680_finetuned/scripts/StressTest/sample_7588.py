scores = [46, 75, 72, 63, 65]
new_scores = [86, 75, 72, 63, 65]

# the hypothesis refers to the same examination with different scores
# the premise gives the average mark for each subject
# the hypothesis gives the average mark for each subject

# calculate the average mark for each subject in the premise
average_mark_premise = sum(scores) / len(scores)

# calculate the average mark for each subject in the hypothesis
average_mark_hypothesis = sum(new_scores) / len(new_scores)

# check if the average mark in the hypothesis contradicts the average mark in the premise
if average_mark_hypothesis!= average_mark_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
