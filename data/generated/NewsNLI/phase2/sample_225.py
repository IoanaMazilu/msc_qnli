# Premise: Reigning champions Borussia Dortmund routed Moenchengladbach 5-0 to rise to third in the table.
# Hypothesis: Borussia Dortmund up to third after 5-0 rout of Moenchengladbach.
# Golden Label: entailment

score_premise = 5
score_hypothesis = 5
table_position_premise = 3
table_position_hypothesis = 3

# the hypothesis mentions the score and the table position of Borussia Dortmund, which are also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif table_position_hypothesis != table_position_premise:
    # check if the table position from the hypothesis contradicts the table position in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

