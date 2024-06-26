pens_total_premise = 22
pens_total_hypothesis = 12

# the hypothesis talks about the total number of pens Elena purchased, which is also mentioned in the premise
if pens_total_hypothesis >= pens_total_premise:
    # check if the hypothesis value contradicts the premise that the total number of pens is less than 'pens_total_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
