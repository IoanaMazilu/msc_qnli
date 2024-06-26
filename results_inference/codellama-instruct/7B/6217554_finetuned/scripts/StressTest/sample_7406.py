lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 8

# the hypothesis talks about the number of lenses in each telescope, referenced also in the premise
if lenses_per_telescope_hypothesis!= lenses_per_telescope_premise:
    # check if the number of lenses in each telescope in the hypothesis contradicts the number of lenses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
