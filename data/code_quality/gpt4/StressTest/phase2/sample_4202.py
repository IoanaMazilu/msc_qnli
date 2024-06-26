months_rakesh_premise = 4
months_rakesh_hypothesis = 4

# the hypothesis talks about the number of months Rakesh stayed, referenced also in the premise
if months_rakesh_hypothesis > months_rakesh_premise:
    # check if the hypothesis value contradicts the estimate of 'months_rakesh_premise'
    label = "contradiction"
elif months_rakesh_hypothesis < months_rakesh_premise:
    # check if the hypothesis value contradicts the estimate of 'months_rakesh_premise'
    label = "entailment"
else:
    # the premise gives only an exact for the number of months
    # any number of months equal to 'months_rakesh_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
