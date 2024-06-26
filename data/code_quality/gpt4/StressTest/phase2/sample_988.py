seniors_premise = 100
seniors_hypothesis = 300
car_owners_premise = 0.5
car_owners_hypothesis = 0.5

# the hypothesis gives a specific number of seniors and their car ownership percentage at Morse High School
if seniors_hypothesis <= seniors_premise or car_owners_hypothesis != car_owners_premise:
    # check if the number of seniors in the hypothesis contradicts the premise
    # or if the car ownership percentage in the hypothesis contradicts the premise
    label = "contradiction"
elif seniors_hypothesis > seniors_premise and car_owners_hypothesis == car_owners_premise:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors greater than 'seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
