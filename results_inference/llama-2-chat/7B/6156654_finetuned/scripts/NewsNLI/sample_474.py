matches_premise = 23
matches_hypothesis = 23

# the hypothesis mentions the number of matches Varane played for Lens, which is also mentioned in the premise
if matches_hypothesis!= matches_premise:
    # check if the number of matches in the hypothesis contradicts the number of matches in the premise
    label = "contradiction"
else:
    # if the number of matches in the hypothesis does not contradict the number of matches in the premise, we can infer entailment
    label = "entailment"

print(label)
