# Premise: He will be less than 8/3 times as old as Tom 6 years hence.
# Hypothesis: He will be 5/3 times as old as Tom 6 years hence.
# Golden Label: neutral

age_ratio_premise = 8/3
age_ratio_hypothesis = 5/3

# the hypothesis talks about the age ratio between 'he' and 'Tom' in the future, referenced also in the premise
if age_ratio_hypothesis >= age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the premise's age ratio being less than 'age_ratio_premise'
    label = "contradiction"
elif age_ratio_hypothesis < age_ratio_premise:
    # the premise states that 'he' will be less than 'age_ratio_premise' times as old as Tom
    # any age ratio less than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the age ratio in the hypothesis is equal to 'age_ratio_premise' we can infer entailment
    label = "entailment"

print(label)

