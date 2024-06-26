doctors_hospital_premise = 10
doctors_hospital_hypothesis = 10

# the hypothesis talks about the number of doctors in the hospital, referenced also in the premise
if doctors_hospital_hypothesis!= doctors_hospital_premise:
    # check if the number of doctors in the hypothesis contradicts the number of doctors in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are consistent with each other
    label = "entailment"

print(label)
