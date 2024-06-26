oa_premise = 2
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis refers to the length of OB, which is not mentioned in the premise
# the hypothesis value of 'oa_hypothesis' contradicts the premise value of 'oa_premise'
if oa_hypothesis > oa_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of OB
    # any length of OB consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
