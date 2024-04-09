def compare_values(premise_value, hypothesis_value):
    if premise_value!= hypothesis_value:
        return "contradiction"
    else:
        return "entailment"

premise_value = -2
hypothesis_value = -2

label = compare_values(premise_value, hypothesis_value)
print(label)
