seniors_premise = 500
seniors_hypothesis = 300
car_owners_premise = 0.5
car_owners_hypothesis = 0.5

# the hypothesis refers to the number of seniors and their car ownership percentage at Morse High School, mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the estimate of less than'seniors_premise'
    label = "contradiction"
elif car_owners_hypothesis!= car_owners_premise:
    # check if the car ownership percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors less than'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)