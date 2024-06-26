graduates_premise = 0.15
graduates_hypothesis = 0.15

# the hypothesis refers to the percentage of college graduates in Amtek's sales staff, which is also mentioned in the premise
if graduates_hypothesis >= graduates_premise:
    # check if the percentage of graduates in the hypothesis contradicts the percentage of graduates in the premise
    label = "contradiction"
else:
    # if the percentage of graduates in the hypothesis is less than the premise, it can be entailed
    label = "entailment"

print(label)
