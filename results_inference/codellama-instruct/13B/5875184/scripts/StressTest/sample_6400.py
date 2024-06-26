premise = "If the number of such passengers that used Miami Airport was less than 8/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?"
hypothesis = "If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?"

# extract the numerical entities from the premise and hypothesis
premise_num_passengers_miami = int(premise.split(" ")[-1])
premise_num_passengers_kennedy = int(premise.split(" ")[-3])
premise_num_passengers_logan = int(premise.split(" ")[-5])
hypothesis_num_passengers_miami = int(hypothesis.split(" ")[-1])
hypothesis_num_passengers_kennedy = int(hypothesis.split(" ")[-3])
hypothesis_num_passengers_logan = int(hypothesis.split(" ")[-5])

# perform the calculations
premise_ratio = premise_num_passengers_miami / (premise_num_passengers_kennedy * 2)
hypothesis_ratio = hypothesis_num_passengers_miami / (hypothesis_num_passengers_kennedy * 2)

# compare the ratios
if premise_ratio < hypothesis_ratio:
    label = "contradiction"
elif premise_ratio == hypothesis_ratio:
    label = "neutral"
else:
    label = "entailment"

print(label)
