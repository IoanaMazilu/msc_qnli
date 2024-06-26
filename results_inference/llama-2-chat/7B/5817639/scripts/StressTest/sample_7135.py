st_premise = 50
tv_premise = 50
sv_premise = 12

# the hypothesis talks about the sides of a triangle, referenced also in the premise
if tv_hypothesis <= tv_premise:
    # check if the hypothesis value contradicts the estimate of 'tv_premise'
    label = "contradiction"
elif st_hypothesis!= st_premise:
    # check if the estimate of'st_hypothesis' contradicts the estimate of'st_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
