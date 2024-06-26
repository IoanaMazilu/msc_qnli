subject1_premise = 55
subject1_hypothesis = 35
subject2_premise = 67
subject2_hypothesis = 67
subject3_premise = 76
subject3_hypothesis = 76
subject4_premise = 82
subject4_hypothesis = 82
subject5_premise = 85
subject5_hypothesis = 85

# the hypothesis talks about the scores obtained by Reeya in different subjects, which are also mentioned in the premise
if subject1_hypothesis!= subject1_premise:
    # check if the score in the hypothesis contradicts the score mentioned in the premise for subject 1
    label = "contradiction"
elif subject2_hypothesis!= subject2_premise or subject3_hypothesis!= subject3_premise or subject4_hypothesis!= subject4_premise or subject5_hypothesis!= subject5_premise:
    # check if the scores in the hypothesis for other subjects contradict the scores mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
