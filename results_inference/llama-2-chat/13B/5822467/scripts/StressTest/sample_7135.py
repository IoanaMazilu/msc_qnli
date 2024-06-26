st_length_premise = less than 50
st_length_hypothesis = 10
tv_length_premise = less than 50
tv_length_hypothesis = 10
sv_length_premise = 12

# the hypothesis refers to the length of the sides of the triangle
if st_length_hypothesis <= st_length_premise and tv_length_hypothesis <= tv_length_premise and sv_length_hypothesis == sv_length_premise:
    # all lengths in the hypothesis are consistent with the premise, so we can infer neutrality
    label = "neutral"
elif st_length_hypothesis > st_length_premise or tv_length_hypothesis > tv_length_premise:
    # at least one side length in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the sides, so we can entail the hypothesis
    label = "entailment"

print(label)
