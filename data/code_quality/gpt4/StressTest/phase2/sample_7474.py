premise_condition = 4
hypothesis_condition = 2

# the hypothesis refers to the condition for a number to be a 'Sophie Germain' prime, also mentioned in the premise
if premise_condition != hypothesis_condition:
    # check if the condition in the hypothesis contradicts the condition stated in the premise
    label = "contradiction"
else:
    # if the conditions are the same, the hypothesis is entailed from the premise
    label = "entailment"

print(label)
