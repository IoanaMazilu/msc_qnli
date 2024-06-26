father_age = 60
ayisha_age = 10

# the hypothesis refers to the age of Ayisha and her father, mentioned in the premise
if ayisha_age >= father_age / 6:
    # check if the estimate of 'father_age / 6' contradicts the age of Ayisha in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Ayisha
    # any age of Ayisha less than 'father_age / 6' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
