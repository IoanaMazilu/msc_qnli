# Premise: The United Nations last night elected eight judges for the international war crimes tribunal that will try those accused of murders and other atrocities in former Yugoslavia since 1991.
# Hypothesis: 11 judges in the Yugoslavia war tribunal were sworn in at the World court.
# Golden Label: neutral

judges_elected_premise = 8
judges_sworn_in_hypothesis = 11

# the hypothesis talks about the number of judges sworn in for a tribunal, which is different from the number of judges elected mentioned in the premise
if judges_sworn_in_hypothesis != judges_elected_premise:
    # check if the number of judges in the hypothesis contradicts the number of judges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

