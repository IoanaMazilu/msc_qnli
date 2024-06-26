premise_start = "2 nd Rd and 3 rd Ave"
premise_end = "10 th Rd and 5 th Ave"
hypothesis_start = "5 nd Rd and 3 rd Ave"
hypothesis_end = "10 th Rd and 5 th Ave"

# check if the hypothesis start and end points are the same as the premise start and end points
if hypothesis_start == premise_start and hypothesis_end == premise_end:
    # if the hypothesis start and end points are the same as the premise start and end points, we can infer entailment
    label = "entailment"
elif hypothesis_start!= premise_start or hypothesis_end!= premise_end:
    # if the hypothesis start and end points are different from the premise start and end points, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis start and end points are not the same as the premise start and end points, but are still consistent with the premise, we can infer neutral
    label = "neutral"

print(label)
