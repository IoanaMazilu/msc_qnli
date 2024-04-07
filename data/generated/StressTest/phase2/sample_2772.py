# Premise: If it takes Annie 15 minutes to fix the flat tire and Sam continues to ride during this time, how many minutes will it take Annie to catch up with Sam assuming that Annie resumes riding at 15 km per hour?
# Hypothesis: If it takes Annie less than 35 minutes to fix the flat tire and Sam continues to ride during this time, how many minutes will it take Annie to catch up with Sam assuming that Annie resumes riding at 15 km per hour?
# Golden Label: entailment

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

