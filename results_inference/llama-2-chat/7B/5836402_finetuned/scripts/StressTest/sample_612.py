gang_size_premise = 8
gang_size_hypothesis = 7

# the hypothesis refers to the size of Andrew's friendship gang mentioned in the premise
if gang_size_hypothesis <= gang_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of Andrew's friendship gang
    # any size greater than 'gang_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
