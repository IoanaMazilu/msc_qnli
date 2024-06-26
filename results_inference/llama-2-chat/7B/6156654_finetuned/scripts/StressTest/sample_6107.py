# the premise gives the current age of Jane, and when she stopped baby-sitting
current_age_premise = 32
stopped_baby_sitting_premise = 12

# the hypothesis gives the current age of Jane and when she stopped baby-sitting
current_age_hypothesis = 32
stopped_baby_sitting_hypothesis = 12

# the hypothesis cannot be entailed from the premise
if current_age_premise == current_age_hypothesis:
    label = "neutral"
elif stopped_baby_sitting_premise!= stopped_baby_sitting_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
