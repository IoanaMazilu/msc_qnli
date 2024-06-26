# define variables for the numerical entities in the premise and hypothesis
band_suspended_premise = 1
band_suspended_hypothesis = 1

# check if the band was suspended in both the premise and hypothesis
if band_suspended_premise == band_suspended_hypothesis:
    # if the band was suspended in both, we can infer entailment
    label = "entailment"
else:
    # if the band was not suspended in both, we can infer contradiction
    label = "contradiction"

print(label)
