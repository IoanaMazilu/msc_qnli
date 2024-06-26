scientific_proof_premise = 6/3
scientific_proof_hypothesis = 4/3

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if scientific_proof_hypothesis!= scientific_proof_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios match, we can infer entailment
    label = "entailment"

print(label)
