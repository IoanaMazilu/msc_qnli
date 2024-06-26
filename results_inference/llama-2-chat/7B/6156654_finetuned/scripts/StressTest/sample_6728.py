apples_premise = 10
apples_hypothesis = 20

# the hypothesis refers to the number of apples and oranges selected by Mary, which is also mentioned in the premise
if apples_hypothesis!= apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the number of apples in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
