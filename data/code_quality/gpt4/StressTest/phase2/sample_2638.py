crayons_additional_boxes_premise = 5
crayons_additional_boxes_hypothesis = 2

# the hypothesis talks about the number of additional boxes of crayons Albert buys, which is also referenced in the premise
if crayons_additional_boxes_hypothesis >= crayons_additional_boxes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'crayons_additional_boxes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of additional boxes of crayons
    # any number of additional boxes less than 'crayons_additional_boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
