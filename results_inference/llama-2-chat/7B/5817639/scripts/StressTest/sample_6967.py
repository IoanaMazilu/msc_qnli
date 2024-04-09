property_size_premise = 800
property_size_hypothesis = 900

# the hypothesis refers to the size of the property mentioned in the premise
if property_size_premise <= property_size_hypothesis:
    # check if the estimate of 'property_size_hypothesis' contradicts the number of square feet in the premise
    label = "contradiction"
elif property_size_hypothesis!= property_size_premise:
    # check if the number of square feet in the hypothesis contradicts the number of square feet reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
