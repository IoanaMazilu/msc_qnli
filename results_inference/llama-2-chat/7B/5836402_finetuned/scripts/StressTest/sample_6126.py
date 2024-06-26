people_iceland_norway_premise = 31
people_iceland_norway_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway, which is also mentioned in the premise
if people_iceland_norway_premise >= people_iceland_norway_hypothesis:
    # check if the estimate of 'people_iceland_norway_hypothesis' contradicts the number of people who visited both countries in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
