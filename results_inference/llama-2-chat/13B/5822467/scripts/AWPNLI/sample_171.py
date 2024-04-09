pencils_premise = 142.0
pencils_given_premise = 31.0
left_pencils_hypothesis = 106.0

# compute the total number of pencils given in the premise
total_pencils_premise = pencils_premise - pencils_given_premise

if left_pencils_hypothesis > total_pencils_premise:
    # the hypothesis implies that Josh has more pencils left than the total number of pencils given in the premise, so there is a contradiction
    label = "contradiction"
elif left_pencils_hypothesis < total_pencils_premise:
    # the hypothesis implies that Josh has fewer pencils left than the total number of pencils given in the premise, so there is entailment
    label = "entailment"
else:
    # if the number of pencils left in the hypothesis is equal to the total number of pencils given in the premise, then there is neither entailment nor contradiction
    label = "neutral"

print(label)
