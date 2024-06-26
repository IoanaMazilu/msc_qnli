y_premise = 810
y_hypothesis = 210

# the hypothesis talks about Michael's earnings, which is also referenced in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the premise that Michael earned less than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings
    # any earnings less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
