premise = "If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?"
hypothesis = "If the number of such passengers that used Miami Airport was 3/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?"

# extract the numerical entities from the premise and hypothesis
premise_miami_airport = 1/2
premise_kennedy_airport = 1/2
premise_logan_airport = 4

hypothesis_miami_airport = 3/2
hypothesis_kennedy_airport = 3/2
hypothesis_logan_airport = 4

# compare the numerical entities in the premise and hypothesis
if premise_miami_airport == hypothesis_miami_airport and premise_kennedy_airport == hypothesis_kennedy_airport and premise_logan_airport == hypothesis_logan_airport:
    # if the numerical entities in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"
elif premise_miami_airport!= hypothesis_miami_airport or premise_kennedy_airport!= hypothesis_kennedy_airport or premise_logan_airport!= hypothesis_logan_airport:
    # if the numerical entities in the premise and hypothesis are different, we can infer contradiction
    label = "contradiction"
else:
    # if the numerical entities in the premise and hypothesis are the same, but the estimates are different, we can infer neutral
    label = "neutral"

print(label)
