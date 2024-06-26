average_score_premise = 86
average_score_hypothesis = 86

# the hypothesis refers to the average score in each subject as mentioned in the premise
for subject in ["French Language", "Geography", "Art and design", "History", "Physical Education"]:
    if average_score_hypothesis <= average_score_premise[subject]:
        # check if the hypothesis value contradicts the premise value for each subject
        label = "contradiction"
        break
    else:
        # if the hypothesis value does not contradict the premise value, we can infer entailment
        label = "entailment"

print(label)
