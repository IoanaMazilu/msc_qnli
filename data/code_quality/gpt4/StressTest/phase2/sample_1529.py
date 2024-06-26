divisions_premise = [5, 6, 9]
divisions_hypothesis = [3, 6, 9]

# the hypothesis talks about the possible divisions of Cook's herd, mentioned also in the premise
if divisions_hypothesis[0] in divisions_premise and divisions_hypothesis[1] in divisions_premise and divisions_hypothesis[2] in divisions_premise:
    # check if the division values in the hypothesis are present in the premise
    label = "entailment"
elif divisions_hypothesis[0] not in divisions_premise or divisions_hypothesis[1] not in divisions_premise or divisions_hypothesis[2] not in divisions_premise:
    # check if any of the division values in the hypothesis contradicts the division values in the premise
    label = "contradiction"
else:
    # any other case, the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
