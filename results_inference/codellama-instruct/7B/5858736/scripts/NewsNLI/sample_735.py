ten_cate_premise = "assistant manager at English Premier League side Chelsea"
ten_cate_hypothesis = "formerly assistant coach at Chelsea and Barcelona"

# the hypothesis mentions a former position at Chelsea, which is also mentioned in the premise
if ten_cate_hypothesis!= ten_cate_premise:
    # check if the former position in the hypothesis contradicts the position in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
