years_back_premise = 6
years_back_hypothesis = 6

# the hypothesis refers to the same situation as in the premise, but the time frame is different
if years_back_hypothesis < years_back_premise:
    # the hypothesis situation is contradicting the premise one
    label = "contradiction"
elif years_back_hypothesis > years_back_premise:
    # the hypothesis situation cannot be entailed from the premise
    label = "neutral"
else:
    # the hypothesis situation is the same as the premise one
    label = "entailment"

print(label)
