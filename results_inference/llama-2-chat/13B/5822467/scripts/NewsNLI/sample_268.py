ministry_premise = "Ministry of Transport"
flights_premise = "Indonesia AirAsia flights"
investigation_hypothesis = "full investigation"
service_suspension_hypothesis = "suspend AirAsia's service"

# extract numerical information
flights_premise_int = int(flights_premise)
investigation_hypothesis_int = int(investigation_hypothesis)
service_suspension_hypothesis_int = int(service_suspension_hypothesis)

# compare quantities
if flights_premise_int!= investigation_hypothesis_int and flights_premise_int!= service_suspension_hypothesis_int:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
elif investigation_hypothesis_int == service_suspension_hypothesis_int:
    # the hypothesis mentions the investigation and service suspension, but does not provide any additional information
    label = "neutral"
else:
    # the hypothesis mentions the investigation and service suspension, which are also mentioned in the premise
    label = "entailment"

print(label)
