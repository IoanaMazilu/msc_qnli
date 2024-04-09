marks_premise = 35
marks_hypothesis = 45

# the hypothesis refers to the mark secured by Reema written as less than 45
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif marks_hypothesis < marks_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the correct average marks
    # any mark less than 45 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
