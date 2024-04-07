# Premise: There are 300 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are less than 500 seniors at Morse High School, and 50% of them have cars.
# Golden Label: entailment

seniors_premise = 300
seniors_hypothesis = 500
car_owners_premise = 0.5 * seniors_premise
car_owners_hypothesis = 0.5 * seniors_hypothesis

# the hypothesis refers to the number of seniors and car owners at Morse High School mentioned in the premise
if seniors_premise > seniors_hypothesis:
    # check if the number of seniors in the premise contradicts the estimate of 'seniors_hypothesis'
    label = "contradiction"
elif car_owners_premise != car_owners_hypothesis:
    # check if the number of car owners in the premise contradicts the estimate of 'car_owners_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

