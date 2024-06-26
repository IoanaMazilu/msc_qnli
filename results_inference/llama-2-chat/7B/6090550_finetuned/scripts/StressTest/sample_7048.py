y_premise = 62
y_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, which is also referenced in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise'
    label = "contradiction"
elif y_hypothesis < y_premise:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is less than 'y_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

