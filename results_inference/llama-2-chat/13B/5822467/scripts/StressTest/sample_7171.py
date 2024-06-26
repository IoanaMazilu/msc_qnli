andy_problems_premise = 30
andy_problems_hypothesis = 70

# the hypothesis refers to the number of problems Andy solves in a Math exercise
if andy_problems_premise <= andy_problems_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'andy_problems_premise'
    label = "contradiction"
elif andy_problems_hypothesis > andy_problems_premise:
    # check if the hypothesis value entails the estimate of 'andy_problems_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the number of problems Andy solves
    # any number of problems greater than 'andy_problems_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
