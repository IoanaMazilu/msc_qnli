horses_premise = 4
horses_hypothesis = 3
total_horses = 25

# the hypothesis talks about the number of fastest horses needed for the Kentucky Derby, referenced also in the premise
if horses_hypothesis >= horses_premise:
    # check if the hypothesis value contradicts the estimate of less than 'horses_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses less than 'horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
