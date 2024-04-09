herd_premise = 4
herd_hypothesis = 5

# the hypothesis refers to the number of equal parts in the herd
if herd_hypothesis <= herd_premise:
    # check if the hypothesis value contradicts the number of equal parts reported in the premise
    label = "contradiction"
elif herd_hypothesis == 6 and herd_premise == 6:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts reported in the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of equal parts
    # any number of equal parts greater than 'herd_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
