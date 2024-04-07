# Premise: Tim has 350 pounds of cement in 100, 50, and 25 pound bags.
# Hypothesis: Tim has less than 350 pounds of cement in 100, 50, and 25 pound bags.
# Golden Label: contradiction

cement_premise = 350
cement_hypothesis = 350

# the hypothesis talks about the weight of cement that Tim has, which is also referenced in the premise
if cement_hypothesis >= cement_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cement_premise'
    label = "contradiction"
else:
    # the premise provides an exact amount of cement that Tim has
    # any amount of cement less than 'cement_premise' can be entailed from the premise
    label = "entailment"

print(label)

