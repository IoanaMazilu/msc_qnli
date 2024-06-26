st_tv_premise = 50
st_tv_hypothesis = 10
sv_premise = 12
sv_hypothesis = 12

# the hypothesis refers to the sides of triangle STV mentioned in the premise
if st_tv_hypothesis >= st_tv_premise:
    # check if the value of'st_tv_hypothesis' contradicts the estimate of less than'st_tv_premise'
    label = "contradiction"
elif sv_hypothesis!= sv_premise:
    # check if the value of'sv_hypothesis' contradicts the value of'sv_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sides of the triangle
    # any sides less than'st_tv_premise' and equal to'sv_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
