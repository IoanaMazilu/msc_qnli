# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be less than 8/3 times as old as Tom 6 years hence.
# Golden Label: entailment

old_ratio_premise = 5/3
old_ratio_hypothesis = 8/3

# the hypothesis talks about the age ratio between 'He' and 'Tom' after 6 years, which is also referenced in the premise
if old_ratio_hypothesis < old_ratio_premise:
    # check if the hypothesis value contradicts the estimate of 'old_ratio_premise'
    label = "contradiction"
else:
    # any age ratio greater than or equal to 'old_ratio_premise' is consistent with the premise
    # but cannot be explicitly entailed from the premise unless it's equal to 'old_ratio_premise'
    label = "neutral" if old_ratio_hypothesis > old_ratio_premise else "entailment"

print(label)

