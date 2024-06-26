golf_tees_premise = 20
golf_tees_hypothesis = 40
packages_limit = 2

# the hypothesis talks about the number of golf tees for each member of Bill's foursome
if golf_tees_hypothesis >= golf_tees_premise:
    # check if the hypothesis value contradicts the minimum limit of 'golf_tees_premise' golf tees for each member
    label = "contradiction"
else:
    # the premise gives a minimum limit for the number of golf tees for each member
    # any number of golf tees less than 'golf_tees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
