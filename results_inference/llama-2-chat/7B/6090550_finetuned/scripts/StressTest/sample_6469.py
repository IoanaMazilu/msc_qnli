 is_neutral = 1

# the hypothesis talks about the percentage of the carpeted area, which is also mentioned in the premise
if carpet_coverage_premise < 20:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
