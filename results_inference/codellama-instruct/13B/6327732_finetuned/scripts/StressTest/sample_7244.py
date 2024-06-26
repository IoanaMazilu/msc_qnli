ayisha_father_age_premise = 10
shankar_age_premise = 10
ayisha_father_age_hypothesis = 30
shankar_age_hypothesis = 30

# the hypothesis refers to the age of Ayisha's father and Shankar after 30 years, which is not mentioned in the premise
if ayisha_father_age_hypothesis!= ayisha_father_age_premise:
    # check if the hypothesis value contradicts the age of Ayisha's father in the premise
    label = "contradiction"
elif shankar_age_hypothesis!= shankar_age_premise:
    # check if the hypothesis value contradicts the age of Shankar in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Ayisha's father and Shankar
    # any number of years greater than 'ayisha_father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
