builder_from_chennai_premise = 2
builder_from_chennai_hypothesis = 3
days_taken_premise = 15

# the hypothesis refers to the builder from Chennai and the number of days taken
if builder_from_chennai_hypothesis <= builder_from_chennai_premise:
    # check if the estimate of 'builder_from_chennai_hypothesis' contradicts the number of builders mentioned in the premise
    label = "contradiction"
elif days_taken_premise!= days_taken_hypothesis:
    # check if the number of days taken in the hypothesis contradicts the number of days taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
