st_premise = 26
tv_premise = 26
sv_premise = 20

st_hypothesis = 66
tv_hypothesis = 66
sv_hypothesis = 20

# the hypothesis talks about the sides of a triangle, referenced also in the premise
if st_hypothesis <= st_premise:
    # check if the hypothesis value contradicts the estimate of'st' in the premise
    label = "contradiction"
elif tv_hypothesis <= tv_premise:
    # check if the hypothesis value contradicts the estimate of 'TV' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the sides, any value less than'st_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
