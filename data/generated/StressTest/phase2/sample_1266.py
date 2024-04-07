# Premise: Martha has 4 dogs and 4 cats.
# Hypothesis: Martha has less than 5 dogs and 4 cats.
# Golden Label: entailment

dogs_martha_premise = 4
dogs_martha_hypothesis = 5
cats_martha_premise = 4
cats_martha_hypothesis = 4

# the hypothesis refers to the number of dogs and cats Martha has, which is also mentioned in the premise
if dogs_martha_premise >= dogs_martha_hypothesis:
    # check if the premise value contradicts the estimate of less than 'dogs_martha_hypothesis'
    label = "contradiction"
elif cats_martha_premise != cats_martha_hypothesis:
    # check if the number of cats Martha has in the hypothesis contradicts the number of cats Martha has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

