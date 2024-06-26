ayisha_age_fraction = 1/6
father_age_fraction = 3/6

# the hypothesis talks about Ayisha's age being less than 3/6 of her father's age
if ayisha_age_fraction >= 3/6:
    label = "contradiction"
else:
    # Ayisha's age is less than 3/6 of her father's age, which is not necessarily a contradiction
    label = "neutral"

print(label)
