john_jose_binoy_premise = 2600
john_jose_binoy_hypothesis = 6600

# the hypothesis refers to the number of people in the ratio 2:4:6 mentioned in the premise
if john_jose_binoy_hypothesis <= john_jose_binoy_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_jose_binoy_premise'
    label = "contradiction"
elif john_jose_binoy_hypothesis!= john_jose_binoy_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
