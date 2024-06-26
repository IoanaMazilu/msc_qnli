# the hypothesis refers to the values of OA, AC and BD mentioned in the premise
if OA <= 2:
    # check if the hypothesis value contradicts the estimate of 'OA' in the premise
    label = "contradiction"
elif AC!= 4 or BD!= 6:
    # check if the values of AC and BD in the hypothesis contradict the values reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of OB
    # any length of OB consistent with the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
