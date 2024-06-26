fix_time_premise = 15
fix_time_hypothesis = 15

# the hypothesis refers to the time Annie takes to fix the tire, mentioned in the premise
if fix_time_hypothesis >= fix_time_premise:
    # check if 'fix_time_hypothesis' contradicts the premise where it must be less than 'fix_time_premise'
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
