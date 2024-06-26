father_age = 60
ayisha_age = 10

# the hypothesis refers to the age of Ayisha and her father, as mentioned in the premise
if ayisha_age >= father_age / 3:
    # check if the estimate of 'ayisha_age' contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Ayisha's age
    # any age of Ayisha less than 'father_age / 3' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
