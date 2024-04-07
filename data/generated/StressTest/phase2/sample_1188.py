# Premise: If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 8 th Rd and 7 th Ave in the shortest possible time, how many different routes could he take?
# Hypothesis: If Bill needs to walk from the corner of less than 3 nd Rd and 3 rd Ave to the corner of 8 th Rd and 7 th Ave in the shortest possible time, how many different routes could he take?
# Golden Label: entailment

start_premise = 2
start_hypothesis = 3

# the hypothesis refers to the starting point of the route mentioned in the premise
if start_hypothesis <= start_premise:
    # check if the starting point in the hypothesis contradicts the starting point mentioned in the premise
    label = "contradiction"
else:
    # if the starting point in the hypothesis does not contradict the starting point in the premise, we can infer entailment
    label = "entailment"

print(label)

