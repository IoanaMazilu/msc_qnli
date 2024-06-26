dogs_martha_premise = 5
cats_martha_premise = 5
dogs_martha_hypothesis = 6
cats_martha_hypothesis = 5

# the hypothesis talks about the number of dogs and cats Martha has, which is also mentioned in the premise
if dogs_martha_hypothesis != dogs_martha_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs reported in the premise
    label = "contradiction"
elif cats_martha_hypothesis != cats_martha_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
