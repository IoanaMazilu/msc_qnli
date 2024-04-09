subject_scores_premise = [40, 60, 70, 80, 80]
subject_scores_hypothesis = [less than 40, less than 60, less than 70, less than 80, less than 80]

# define variables for the premise and hypothesis
average_premise = sum(subject_scores_premise) / len(subject_scores_premise)
average_hypothesis = sum(subject_scores_hypothesis) / len(subject_scores_hypothesis)

# compare the averages
if average_premise <= average_hypothesis:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif average_hypothesis!= average_premise:
    # the hypothesis does not contradict the premise, but cannot be fully entailed from the premise
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
