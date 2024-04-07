# Premise: If it takes Pat 20 minutes to stretch and Cara continues to run during this time, how many minutes will it take Pat to catch up to Cara?
# Hypothesis: If it takes Pat 80 minutes to stretch and Cara continues to run during this time, how many minutes will it take Pat to catch up to Cara?
# Golden Label: contradiction

pat_stretch_time_premise = 20
pat_stretch_time_hypothesis = 80

# the hypothesis and premise both refer to the time it takes Pat to stretch
if pat_stretch_time_premise != pat_stretch_time_hypothesis:
    # check if the time it takes for Pat to stretch in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the stretch times in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)

