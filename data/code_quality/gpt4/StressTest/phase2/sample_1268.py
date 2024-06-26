dogs_martha_premise = 4
dogs_martha_hypothesis = 3
cats_martha_premise = 4
cats_martha_hypothesis = 4

# the hypothesis talks about the number of dogs and cats Martha has, referenced also in the premise
if dogs_martha_hypothesis != dogs_martha_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs reported in the premise
    label = "contradiction"
elif cats_martha_hypothesis != cats_martha_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
