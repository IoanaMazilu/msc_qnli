# Premise: In an exam, Libi scored 78 percent, Nibi scored 75 percent and Catherine 85 percent.
# Hypothesis: In an exam, Libi scored 48 percent, Nibi scored 75 percent and Catherine 85 percent.
# Golden Label: contradiction

libi_score_premise = 78
nibi_score_premise = 75
catherine_score_premise = 85

libi_score_hypothesis = 48
nibi_score_hypothesis = 75
catherine_score_hypothesis = 85

# the hypothesis refers to the scores of Libi, Nibi, and Catherine in an exam, mentioned also in the premise
if libi_score_premise != libi_score_hypothesis:
    # check if Libi's score in the hypothesis contradicts Libi's score in the premise
    label = "contradiction"
elif nibi_score_premise != nibi_score_hypothesis or catherine_score_premise != catherine_score_hypothesis:
    # check if Nibi's score or Catherine's score in the hypothesis contradicts their scores in the premise
    label = "contradiction"
else:
    # if all the scores in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

