# Premise: In an exam, Gibi scored 59 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Hypothesis: In an exam, Gibi scored more than 49 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Golden Label: entailment

gibi_score_premise = 59
gibi_score_hypothesis = 49
jigi_score_premise = 55
jigi_score_hypothesis = 55
mike_score_premise = 99
mike_score_hypothesis = 99
lizzy_score_premise = 67
lizzy_score_hypothesis = 67

# the hypothesis refers to the scores of Gibi, Jigi, Mike, and Lizzy mentioned in the premise
if gibi_score_premise <= gibi_score_hypothesis:
    # check if the estimate of 'gibi_score_hypothesis' contradicts the score of Gibi in the premise
    label = "contradiction"
elif jigi_score_premise != jigi_score_hypothesis:
    # check if the score of Jigi in the hypothesis contradicts the score of Jigi in the premise
    label = "contradiction"
elif mike_score_premise != mike_score_hypothesis:
    # check if the score of Mike in the hypothesis contradicts the score of Mike in the premise
    label = "contradiction"
elif lizzy_score_premise != lizzy_score_hypothesis:
    # check if the score of Lizzy in the hypothesis contradicts the score of Lizzy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

