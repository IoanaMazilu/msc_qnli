cans_paint_premise = 8
cans_paint_hypothesis = 4

# the hypothesis talks about the number of cans of paint Diane finds, referenced also in the premise
if cans_paint_hypothesis <= cans_paint_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cans_paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cans
    # any number of cans less than 'cans_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
