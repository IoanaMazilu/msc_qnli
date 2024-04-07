# Premise: Ayisha's age is less than 3/6 th of her father's age.
# Hypothesis: Ayisha's age is 1/6 th of her father's age.
# Golden Label: neutral

ayisha_age_ratio_premise = 3/6
ayisha_age_ratio_hypothesis = 1/6

# the hypothesis talks about the ratio of Ayisha's age to her father's age
if ayisha_age_ratio_hypothesis >= ayisha_age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ayisha_age_ratio_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

