math_premise = 46
math_hypothesis = 76
sci_premise = 65
sci_hypothesis = 65
soc_premise = 82
soc_hypothesis = 82
eng_premise = 67
eng_hypothesis = 75
bio_premise = 75
bio_hypothesis = 75

# check if the hypothesis values contradict the premise values
if math_hypothesis < math_premise:
    label = "contradiction"
elif sci_hypothesis < sci_premise:
    label = "contradiction"
elif soc_hypothesis < soc_premise:
    label = "contradiction"
elif eng_hypothesis < eng_premise:
    label = "contradiction"
elif bio_hypothesis < bio_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
