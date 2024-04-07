# Premise: Antony can divide his herd into more than 4 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: Antony can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: neutral

herd_parts_premise = 4
herd_parts_hypothesis = 5
herd_parts_equal_premise = 6
herd_parts_equal_hypothesis = 6
herd_parts_not_premise = 9
herd_parts_not_hypothesis = 9

# the hypothesis talks about the number of equal parts Antony can divide his herd into, referenced also in the premise
if herd_parts_hypothesis <= herd_parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'herd_parts_premise'
    label = "contradiction"
elif herd_parts_equal_hypothesis != herd_parts_equal_premise or herd_parts_not_hypothesis != herd_parts_not_premise:
    # check if the number of equal parts or the number of non-equal parts in the hypothesis contradicts the numbers reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of equal parts
    # any number of equal parts greater than 'herd_parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

