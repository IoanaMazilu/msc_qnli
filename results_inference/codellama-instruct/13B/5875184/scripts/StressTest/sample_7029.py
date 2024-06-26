premise = "If Bill needs to walk from the corner of 2 nd Rd and 3 rd Ave to the corner of 9 th Rd and 6 th Ave in the shortest possible time, how many different routes could he take?"
hypothesis = "If Bill needs to walk from the corner of less than 7 nd Rd and 3 rd Ave to the corner of 9 th Rd and 6 th Ave in the shortest possible time, how many different routes could he take?"

# extract the numerical entities from the premise and hypothesis
premise_num_routes = int(premise.split(" ")[-1])
hypothesis_num_routes = int(hypothesis.split(" ")[-1])

# check if the hypothesis value contradicts the premise value
if hypothesis_num_routes > premise_num_routes:
    label = "contradiction"
else:
    label = "neutral"

print(label)
