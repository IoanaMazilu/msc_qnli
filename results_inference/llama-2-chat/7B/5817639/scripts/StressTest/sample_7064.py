st_premise = 26
tv_premise = 20
sv_premise = 20

# the hypothesis talks about the sides of a triangle, referenced also in the premise
if tv_hypothesis < tv_premise:
    # check if the hypothesis value contradicts the estimate of 'tv_premise'
    label = "contradiction"
elif sv_hypothesis < sv_premise:
    # check if the hypothesis value contradicts the estimate of'sv_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
