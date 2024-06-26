rank_premise = 65
rank_hypothesis = 15

# the hypothesis talks about the rank of Veena in a class of 182
if rank_hypothesis > rank_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif rank_premise == rank_hypothesis:
    # the premise and hypothesis values are the same, so there is no contradiction or entailment
    label = "neutral"
else:
    # the premise value is less than the hypothesis value, so the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
