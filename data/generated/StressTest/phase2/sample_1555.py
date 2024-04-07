# Premise: In an exam, Gibi scored more than 49 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Hypothesis: In an exam, Gibi scored 59 percent, Jigi scored 55 percent, Mike scored 99 percent and Lizzy 67 percent.
# Golden Label: neutral

gibi_score_premise = 49
gibi_score_hypothesis = 59
jigi_score_premise = 55
jigi_score_hypothesis = 55
mike_score_premise = 99
mike_score_hypothesis = 99
lizzy_score_premise = 67
lizzy_score_hypothesis = 67

# the hypothesis talks about the scores of Gibi, Jigi, Mike and Lizzy in an exam, which are also mentioned in the premise
if gibi_score_hypothesis <= gibi_score_premise:
    # check if Gibi's score in the hypothesis contradicts the estimate of more than 'gibi_score_premise'
    label = "contradiction"
elif jigi_score_hypothesis != jigi_score_premise or mike_score_hypothesis != mike_score_premise or lizzy_score_hypothesis != lizzy_score_premise:
    # check if the scores of Jigi, Mike and Lizzy in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # Gibi's score in the premise is an estimate, while the scores of Jigi, Mike and Lizzy are specific
    # any score for Gibi greater than 'gibi_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    # for Jigi, Mike and Lizzy, the scores in the hypothesis are exactly the same as in the premise
    label = "neutral"

print(label)

