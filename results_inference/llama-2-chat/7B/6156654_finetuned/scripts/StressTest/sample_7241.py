ayisha_age_fraction = 1/6
ayisha_age_fraction_hypothesis = 1/6

# the hypothesis refers to the same age fraction as the premise, but with a different comparison
if ayisha_age_fraction_hypothesis!= ayisha_age_fraction:
    # check if the age fraction in the hypothesis contradicts the age fraction in the premise
    label = "contradiction"
else:
    # if the age fraction in the hypothesis is the same as in the premise, it is a neutral case
    label = "neutral"

print(label)
