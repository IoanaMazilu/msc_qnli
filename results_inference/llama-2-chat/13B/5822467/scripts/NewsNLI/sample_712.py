premise_value = 100000
hypothesis_value = 100000

# the premise and hypothesis both mention the value of the souvenirs, which is the same

# check if the origin of the souvenirs in the hypothesis contradicts the origin of the souvenirs in the premise
if hypothesis_value.origin!= premise_value.origin:
    # if the origins contradict, the hypothesis cannot be entailed from the premise
    label = "contradiction"
else:
    # if the origins are the same, the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
