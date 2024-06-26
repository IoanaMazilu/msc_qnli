oa_premise = 6
oa_hypothesis = 2
ac_premise = 4
ac_hypothesis = 4
bd_premise = 6
bd_hypothesis = 6

# the hypothesis talks about the lengths of OA, AC, and BD, referenced also in the premise
if oa_hypothesis >= oa_premise:
    # check if the hypothesis value contradicts the estimate of less than 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise or bd_hypothesis!= bd_premise:
    # check if the lengths of AC or BD in the hypothesis contradict the lengths reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of OA
    # any length of OA less than 'oa_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
