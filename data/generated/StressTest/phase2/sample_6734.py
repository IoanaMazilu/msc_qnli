# Premise: If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 10 th Rd and 5 th Ave in the shortest possible time, how many different routes could he take?
# Hypothesis: If Bill needs to walk from the corner of 5 nd Rd and 3 rd Ave to the corner of 10 th Rd and 5 th Ave in the shortest possible time, how many different routes could he take?
# Golden Label: contradiction

start_premise_rd = 2
start_premise_ave = 3
end_premise_rd = 10
end_premise_ave = 5

start_hypothesis_rd = 5
start_hypothesis_ave = 3
end_hypothesis_rd = 10
end_hypothesis_ave = 5

# hypothesis and premise both speak about the routes Bill could take from one corner to another
if start_premise_rd != start_hypothesis_rd or start_premise_ave != start_hypothesis_ave or end_premise_rd != end_hypothesis_rd or end_premise_ave != end_hypothesis_ave:
    # if the start or end points of the route in the hypothesis are not the same as in the premise, we have a contradiction
    label = "contradiction"
else:
    # if the start and end points are the same in both premise and hypothesis, we can infer entailment
    label = "entailment"

print(label)

