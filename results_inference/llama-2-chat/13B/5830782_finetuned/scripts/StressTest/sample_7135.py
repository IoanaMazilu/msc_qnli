st_tv_premise = 50
st_tv_hypothesis = 10
sv_premise = 12
sv_hypothesis = 12

# the hypothesis talks about the sides of the same triangle mentioned in the premise
if st_tv_hypothesis > st_tv_premise:
    # check if the length of sides ST and TV in the hypothesis contradicts the premise's maximum length
    label = "contradiction"
elif sv_hypothesis!= sv_premise:
    # check if the length of side SV in the hypothesis contradicts the length of side SV in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the lengths of sides ST and TV
    # any length less than'st_tv_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
