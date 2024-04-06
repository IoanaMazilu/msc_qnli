# Premise: Lepore said he was moved to photograph the slumbering sentries after witnessing the same guard napping on three occasions.
# Hypothesis: Joey Lepore says he took photos of one guard sleeping at post three times.
# Golden Label: entailment

sentries_sleeping_premise = 1
occasions_premise = 3
sentries_sleeping_hypothesis = 1
occasions_hypothesis = 3

# the hypothesis mentions the number of sentries sleeping and the number of times this was observed, which are also mentioned in the premise
if sentries_sleeping_hypothesis != sentries_sleeping_premise:
    # check if the number of sleeping sentries in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif occasions_hypothesis != occasions_premise:
    # check if the number of occasions from the hypothesis contradicts the number of occasions in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

