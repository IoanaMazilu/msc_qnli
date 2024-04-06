# Premise: The junior ranger asked Christian to help him place 420.0 seedlings in packets, and every packet needs to contain 7.0 seeds.
# Hypothesis: They need 60.0 packets.
# Golden Label: entailment

seedlings_premise = 420.0
seeds_per_packet_premise = 7.0
packets_hypothesis = 60.0

# the hypothesis refers to the number of packets needed, which can be computed from the premise
# calculate the number of packets needed according to the premise
packets_premise = seedlings_premise / seeds_per_packet_premise
if packets_hypothesis != packets_premise:
    # check if the number of packets in the hypothesis contradicts the number of packets computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

