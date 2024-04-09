oranges_premise = 0
oranges_hypothesis = 0

# the hypothesis talks about the number of oranges Mary must put back to achieve a different average price than in the premise
if oranges_hypothesis <= oranges_premise:
    # check if the hypothesis value contradicts the estimate of 'oranges_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of oranges
    # any number of oranges greater than 'oranges_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
