premise = "A report prepared by a five member UN commission noted '' killing of civilians, enforced disappearances, destruction of villages, rape and other forms of sexual violence, pillaging and forced displacement, throughout Darfur'', and secretly named alleged war criminals that should go before the ICC."
hypothesis = "More than 200,000 people were killed in the air attack in the Darfur region."

# extract the numerical entities from the premise
premise_num_entities = re.findall(r'\d+', premise)
premise_num_entities = [int(entity) for entity in premise_num_entities]

# extract the numerical entities from the hypothesis
hypothesis_num_entities = re.findall(r'\d+', hypothesis)
hypothesis_num_entities = [int(entity) for entity in hypothesis_num_entities]

# compare the numerical entities between the premise and the hypothesis
if hypothesis_num_entities[0] > premise_num_entities[0]:
    # the hypothesis mentions a higher number of deaths than the premise
    label = "entailment"
elif hypothesis_num_entities[0] < premise_num_entities[0]:
    # the hypothesis mentions a lower number of deaths than the premise
    label = "contradiction"
else:
    # the hypothesis mentions the same number of deaths as the premise
    label = "neutral"

print(label)
