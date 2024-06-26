property_size_last_year = 700
property_size_hypothesis = 700

# the hypothesis refers to the same locality and the same time period as the premise
if property_size_last_year!= property_size_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
