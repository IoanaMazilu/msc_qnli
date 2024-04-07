# Premise: There are less than 500 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are 300 seniors at Morse High School, and 50% of them have cars.
# Golden Label: neutral

seniors_premise = 500
seniors_hypothesis = 300
car_ownership_premise = 0.5
car_ownership_hypothesis = 0.5

# the hypothesis discusses about the number of seniors at Morse High School and their car ownership
# both of these aspects are also mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the estimate of less than 'seniors_premise'
    label = "contradiction"
elif car_ownership_hypothesis != car_ownership_premise:
    # check if the car ownership rate in the hypothesis contradicts the car ownership rate given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    # any number of seniors less than 'seniors_premise' and car ownership rate equal to 'car_ownership_premise' is consistent with the premise
    label = "entailment"

print(label)

