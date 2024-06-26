years_ago_premise = 8
years_ago_hypothesis = 7
times_older = 12

# the hypothesis refers to the same situation as the premise, with different time frames
if years_ago_hypothesis >= years_ago_premise:
    # check if the 'years_ago_hypothesis' contradicts the exact time frame in the premise
    label = "contradiction"
else:
    # if the hypothesis time frame does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
