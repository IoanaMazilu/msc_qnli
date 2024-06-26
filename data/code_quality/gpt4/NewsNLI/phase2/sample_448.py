record_premise = (15, 6)
record_hypothesis = (15, 6)
strikeouts_premise = 197
strikeouts_hypothesis = 197
era_premise = 3.16
era_hypothesis = 3.16

# the hypothesis mentions the pitcher's record, strikeouts, and ERA, which are also mentioned in the premise
if record_hypothesis != record_premise:
    # check if the record in the hypothesis contradicts the record reported in the premise
    label = "contradiction"
elif strikeouts_hypothesis != strikeouts_premise:
    # check if the number of strikeouts from the hypothesis contradicts the number of strikeouts in the premise
    label = "contradiction"
elif era_hypothesis != era_premise:
    # check if the ERA from the hypothesis contradicts the ERA in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
