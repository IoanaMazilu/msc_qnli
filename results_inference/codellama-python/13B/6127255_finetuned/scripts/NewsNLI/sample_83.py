# spokesmen_premise = 2
# spokesmen_hypothesis = 2
# denial_premise = 1
# denial_hypothesis = 1

# # the hypothesis mentions the number of spokesmen who deny the report and the number of spokesmen who confirm it, which are also mentioned in the premise
# if spokesmen_hypothesis!= spokesmen_premise:
#     # check if the number of spokesmen in the hypothesis contradicts the number of spokesmen reported in the premise
#     label = "contradiction"
# elif denial_hypothesis!= denial_premise:
#     # check if the number of spokesmen who deny the report from the hypothesis contradicts the number of spokesmen who deny the report in the premise
#     label = "contradiction"
# else:
#     # if the hypothesis values do not contradict the premise values, we can infer entailment
#     label = "entailment"

# print(label)
# 