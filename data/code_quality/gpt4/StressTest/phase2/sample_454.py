son_lifespan_premise = 5/2
son_lifespan_hypothesis = 1/2

# the hypothesis talks about the son's lifespan relative to Adam's, referenced also in the premise
if son_lifespan_hypothesis >= son_lifespan_premise:
    # check if the hypothesis value contradicts the estimate of less than 'son_lifespan_premise'
    label = "contradiction"
elif son_lifespan_hypothesis == son_lifespan_premise:
    # check if the hypothesis value exactly equals the estimate of 'son_lifespan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the son's lifespan relative to Adam's
    # any lifespan less than 'son_lifespan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
