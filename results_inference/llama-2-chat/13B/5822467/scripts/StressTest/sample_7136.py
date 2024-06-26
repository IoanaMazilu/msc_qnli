st_premise = 10
tv_premise = 10
sv_premise = 12

st_hypothesis = 70
tv_hypothesis = 70
sv_hypothesis = 12

# the hypothesis talks about the lengths of the sides of the triangle
if st_hypothesis <= st_premise and tv_hypothesis <= tv_premise and sv_hypothesis == sv_premise:
    # the hypothesis values are consistent with the premise values, so we can infer entailment
    label = "entailment"
elif st_hypothesis > st_premise or tv_hypothesis > tv_premise or sv_hypothesis!= sv_premise:
    # the hypothesis values contradict the premise values, so we can infer contradiction
    label = "contradiction"
else:
    # the hypothesis values are not consistent with the premise values, but we cannot infer entailment or contradiction
    label = "neutral"

print(label)
