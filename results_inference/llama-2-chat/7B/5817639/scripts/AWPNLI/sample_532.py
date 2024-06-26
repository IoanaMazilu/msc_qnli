passed_premise = 105.0
children_premise = 698.0
children_hypothesis = 593.0

# compare the number of children who passed and the number of children who had to sit it again
if passed_hypothesis >= passed_premise:
    label = "entailment"
elif children_hypothesis > children_premise:
    label = "contradiction"
else:
    label = "contradiction"

print(label)
