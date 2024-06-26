builder_from_chennai_premise = 2
builder_from_chennai_hypothesis = 2
days_builder_premise = 15
days_builder_hypothesis = 15

# the hypothesis refers to the number of days the builder from Chennai takes to build the homes, which is also mentioned in the premise
if builder_from_chennai_hypothesis!= builder_from_chennai_premise:
    # check if the number of days the builder from Chennai takes to build the homes in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
elif days_builder_hypothesis!= days_builder_premise:
    # check if the number of days the builder from Chennai takes to build the homes in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
