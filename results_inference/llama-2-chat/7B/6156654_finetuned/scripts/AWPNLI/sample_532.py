children_test = 698.0
passed_children = 105.0
retake_children = 593.0

# the hypothesis refers to the number of children who had to retake the test, which is also mentioned in the premise
# the hypothesis value is greater than the passed children value
if passed_children <= retake_children:
    label = "contradiction"
else:
    label = "entailment"

print(label)
