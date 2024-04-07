# Premise: If it takes Annie less than 35 minutes to fix the flat tire and Sam continues to ride during this time, how many minutes will it take Annie to catch up with Sam assuming that Annie resumes riding at 15 km per hour?
# Hypothesis: If it takes Annie 15 minutes to fix the flat tire and Sam continues to ride during this time, how many minutes will it take Annie to catch up with Sam assuming that Annie resumes riding at 15 km per hour?
# Golden Label: neutral

fix_time_premise = 35
fix_time_hypothesis = 15

# the hypothesis talks about the time Annie takes to fix the flat tire, which is also referenced in the premise
if fix_time_hypothesis >= fix_time_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'fix_time_premise'
    label = "contradiction"
elif fix_time_hypothesis < fix_time_premise:
    # the hypothesis value is less than the premise estimate, which is consistent but cannot be fully entailed from the premise
    label = "neutral"

print(label)

