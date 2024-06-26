start_rd_premise = 2
start_rd_hypothesis = 7
start_ave_premise = 3
start_ave_hypothesis = 3
end_rd_premise = 9
end_rd_hypothesis = 9
end_ave_premise = 6
end_ave_hypothesis = 6

# The hypothesis refers to the same route as the premise, but the starting road is different
if start_rd_hypothesis >= start_rd_premise:
    # check if the starting road in the hypothesis contradicts the starting road in the premise
    label = "contradiction"
elif start_ave_hypothesis != start_ave_premise or end_rd_hypothesis != end_rd_premise or end_ave_hypothesis != end_ave_premise:
    # check if the starting avenue, ending road, or ending avenue in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
