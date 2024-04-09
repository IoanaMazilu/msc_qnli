seniors_premise = 500
seniors_hypothesis = 300
car_owners_percentage_premise = 50
car_owners_percentage_hypothesis = 50

# the hypothesis refers to the number of seniors and car owners at Morse High School mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the estimate of less than'seniors_premise'
    label = "contradiction"
elif car_owners_percentage_hypothesis!= car_owners_percentage_premise:
    # check if the percentage of car owners in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors less than'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
