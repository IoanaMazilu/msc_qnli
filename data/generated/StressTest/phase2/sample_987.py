# Premise: There are 300 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are more than 100 seniors at Morse High School, and 50% of them have cars.
# Golden Label: entailment

seniors_premise = 300
seniors_hypothesis = 100
car_owners_premise = 0.5 * seniors_premise
car_owners_hypothesis = 0.5 * seniors_hypothesis

# the hypothesis refers to the number of seniors and car owners at Morse High School, which are also mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the estimate of 'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif car_owners_hypothesis != car_owners_premise:
    # check if the number of car owners in the hypothesis contradicts the number of car owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

