jim_cleans_premise = 6
jim_cleans_hypothesis = 5

# the hypothesis refers to the time taken by Jim to clean the entire house
if jim_cleans_hypothesis <= jim_cleans_premise:
    # check if the hypothesis value contradicts the estimate of 'jim_cleans_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Jim
    # any time less than or equal to 'jim_cleans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
