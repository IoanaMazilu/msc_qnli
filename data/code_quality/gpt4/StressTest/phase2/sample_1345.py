hitesh_age_premise = 20
ronnie_age_premise = 60
hitesh_age_hypothesis = 40
ronnie_age_hypothesis = 60

# the hypothesis mentions the ages of Hitesh and Ronnie, which are also mentioned in the premise
if hitesh_age_hypothesis <= hitesh_age_premise:
    # check if the age of Hitesh in the hypothesis contradicts the estimate of more than 'hitesh_age_premise' years old
    label = "contradiction"
elif ronnie_age_hypothesis != ronnie_age_premise:
    # check if the age of Ronnie in the hypothesis contradicts the exact age of Ronnie in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Hitesh
    # any age greater than 'hitesh_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
