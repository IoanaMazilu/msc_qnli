subject_scores_premise = [55, 67, 76, 82, 85]
subject_scores_hypothesis = [35, 67, 76, 82, 85]

# define variables for each subject score
subject_scores = [0, 0, 0, 0, 0]

# iterate through each subject score in the premise
for i, score in enumerate(subject_scores_premise):
    # assign the score to the corresponding variable
    subject_scores[i] = score

# iterate through each subject score in the hypothesis
for i, score in enumerate(subject_scores_hypothesis):
    # check if the score in the hypothesis is less than or equal to the score in the premise
    if score <= subject_scores[i]:
        # if the score in the hypothesis is less than or equal to the score in the premise,
        # it contradicts the premise
        label = "contradiction"
        break

    # if the score in the hypothesis is greater than the score in the premise,
    # it entails the premise
    else:
        label = "entailment"
        break

# if no contradiction was found, the hypothesis is neutral
else:
    label = "neutral"

print(label)
