essential_premise_men_premise = 600
essential_hypothesis_men_hypothesis = 100

# the hypothesis talks about the number of men employed by NHAI to build a highway, which is also mentioned in the premise
if essential_hypothesis_men_hypothesis >= essential_premise_men_premise:
    # check if the hypothesis value contradicts the estimate of less than 'essential_premise_men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than 'essential_premise_men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
