ayisha_age_premise = 1/6
ayisha_age_hypothesis = 3/6

# the hypothesis refers to Ayisha's age in relation to her father's age, also mentioned in the premise
if ayisha_age_premise >= ayisha_age_hypothesis:
    # check if the estimate of 'ayisha_age_premise' contradicts the hypothesis that Ayisha's age is less than 3/6 th of her father's age
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
