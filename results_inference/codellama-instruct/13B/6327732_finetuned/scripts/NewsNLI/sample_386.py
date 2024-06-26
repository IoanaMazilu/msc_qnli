name_premise = "Craig Hicks"
age_premise = 46
crime_premise = "first-degree murder"

name_hypothesis = "Craig Hicks"
crime_hypothesis = "first-degree murder"

# check if the name and crime mentioned in the hypothesis are the same as in the premise
if name_hypothesis == name_premise and crime_hypothesis == crime_premise:
    # if the name and crime are the same, we can infer entailment
    label = "entailment"
else:
    # if the name and crime are not the same, we can infer contradiction
    label = "contradiction"

print(label)
