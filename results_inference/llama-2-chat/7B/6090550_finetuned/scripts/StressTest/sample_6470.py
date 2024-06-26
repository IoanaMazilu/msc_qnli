carpet_coverage_premise = 20
carpet_coverage_hypothesis = 40
carpet_size = 4 # feet
carpet_size_hypothesis = 4 # feet

# the hypothesis talks about the percentage of floor covered by a carpet, which is also mentioned in the premise
if carpet_coverage_hypothesis!= carpet_coverage_premise:
    # check if the percentage of floor covered by carpet in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
