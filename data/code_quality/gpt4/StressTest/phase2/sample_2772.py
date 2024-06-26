fix_time_premise = 15
fix_time_hypothesis = 35

# the hypothesis talks about the time it takes Annie to fix a flat tire, referenced also in the premise
if fix_time_hypothesis < fix_time_premise:
    # check if the hypothesis value contradicts the estimate of 'fix_time_premise'
    label = "contradiction"
elif fix_time_hypothesis == fix_time_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the fix time
    # any fix time greater than 'fix_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
