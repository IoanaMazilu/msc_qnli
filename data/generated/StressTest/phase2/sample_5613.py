# Premise: In an exam, Libi scored 78 percent, Nibi scored 75 percent and Catherine 85 percent.
# Hypothesis: In an exam, Libi scored more than 68 percent, Nibi scored 75 percent and Catherine 85 percent.
# Golden Label: entailment

libi_score_premise = 78
libi_score_hypothesis = 68
nibi_score_premise = 75
nibi_score_hypothesis = 75
catherine_score_premise = 85
catherine_score_hypothesis = 85

# the hypothesis refers to the exam scores of Libi, Nibi and Catherine mentioned in the premise
if libi_score_premise <= libi_score_hypothesis:
    # check if the estimate of 'libi_score_hypothesis' contradicts the score of Libi in the premise
    label = "contradiction"
elif nibi_score_premise != nibi_score_hypothesis:
    # check if the score of Nibi in the hypothesis contradicts the score of Nibi in the premise
    label = "contradiction"
elif catherine_score_premise != catherine_score_hypothesis:
    # check if the score of Catherine in the hypothesis contradicts the score of Catherine in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

