rulers_premise = 11.0
crayons_premise = 34.0
rulers_hypothesis = 25.0

# compute the total number of rulers in the premise
total_rulers_premise = rulers_premise + rulers_hypothesis

# check if the number of rulers in the hypothesis contradicts the number of rulers in the premise
if rulers_hypothesis > total_rulers_premise:
    label = "contradiction"
elif crayons_premise!= crayons_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
