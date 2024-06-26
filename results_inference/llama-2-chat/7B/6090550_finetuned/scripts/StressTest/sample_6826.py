# the premise gives a ratio of ages between Arun and Deepak
# the hypothesis gives a specific ratio of ages between Arun and Deepak

# the hypothesis talks about the ratio of ages between Arun and Deepak
# which is also mentioned in the premise
if ratio_ages_premise!= ratio_ages_hypothesis:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the ratios match, we can infer entailment
    label = "entailment"

print(label)
