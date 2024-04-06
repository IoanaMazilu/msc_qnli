# Premise: Champions League new boys Malaga sealed their passage to the knockout stage with a 1-1 draw at seven-time champions AC Milan in Group C.
# Hypothesis: Malaga qualify from Group C with 1-1 draw at AC Milan.
# Golden Label: entailment

score_premise = 1.5
score_hypothesis = 1.5
group_premise = 'C'
group_hypothesis = 'C'

# the hypothesis mentions the score of the match and the group in which Malaga played, which are also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif group_hypothesis != group_premise:
    # check if the group from the hypothesis contradicts the group in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

