arun_deepak_ratio_premise = 5/5
arun_deepak_ratio_hypothesis = 4/5

# the hypothesis talks about the current age ratio of Arun to Deepak, which is also discussed in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the hypothesis value contradicts the premise's estimate of being less than 'arun_deepak_ratio_premise'
    label = "contradiction"
else:
    # since the hypothesis ratio is less than 'arun_deepak_ratio_premise', it is consistent with the premise, which is therefore entailed
    label = "entailment"

print(label)
