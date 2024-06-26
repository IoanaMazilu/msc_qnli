father_age = 60
ayisha_age = 10

# the hypothesis refers to the age of Ayisha and her father, as mentioned in the premise
if ayisha_age >= 3/6 * father_age:
    # check if the estimate of 'ayisha_age' contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Ayisha and her father
    # any age of Ayisha less than 3/6 th of her father's age is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
