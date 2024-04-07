# Premise: In an exam, Gibi scored 59 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Hypothesis: In an exam, Gibi scored more than 59 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Golden Label: contradiction

gibi_score_premise = 59
gibi_score_hypothesis = 59
jigi_score_premise = 55
jigi_score_hypothesis = 55
mike_score_premise = 99
mike_score_hypothesis = 99
lizzy_score_premise = 67
lizzy_score_hypothesis = 67

# the hypothesis refers to the exam scores of Gibi, Jigi, Mike and Lizzy mentioned in the premise
if gibi_score_hypothesis <= gibi_score_premise:
    # check if the hypothesis contradicts the score of Gibi in the premise
    label = "contradiction"
elif jigi_score_hypothesis != jigi_score_premise or mike_score_hypothesis != mike_score_premise or lizzy_score_hypothesis != lizzy_score_premise:
    # check if the scores of Jigi, Mike or Lizzy in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives exact scores for Gibi, Jigi, Mike and Lizzy
    # the hypothesis saying Gibi scored more than his premise score cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

