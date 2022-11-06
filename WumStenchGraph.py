import pomegranate
import numpy

class WumStechGraph():
        
    wumpus_loc_prob = pomegranate.distributions.DiscreteDistribution({'1_2': 1./15, '1_3': 1./15, '1_4': 1./15, \
    '2_1': 1./15, '2_2': 1./15, '2_3': 1./15, '2_4': 1./15,\
    '3_1': 1./15, '3_2': 1./15, '3_3': 1./15, '3_4': 1./15,\
    '4_1': 1./15, '4_2': 1./15, '4_3': 1./15, '4_4': 1./15})

    # 1_1
    stench_loc_1_1 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 1.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 1.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 0.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 0.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])

    # 1_2
    stench_loc_1_2 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 1.0 ],
            [ '1_3', 'T', 1.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 1.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 0.0 ],
            [ '1_3', 'F', 0.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 0.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 1_3
    stench_loc_1_3 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 1.0 ],
            [ '1_3', 'T', 1.0 ],
            [ '1_4', 'T', 1.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 1.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 0.0 ],
            [ '1_3', 'F', 0.0 ],
            [ '1_4', 'F', 0.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 0.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 1_4
    stench_loc_1_4 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 1.0 ],
            [ '1_4', 'T', 1.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 1.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 0.0 ],
            [ '1_4', 'F', 0.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 0.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 2_1
    stench_loc_2_1 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 1.0 ],
            [ '2_2', 'T', 1.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 1.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 0.0 ],
            [ '2_2', 'F', 0.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 0.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 2_2
    stench_loc_2_2 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 1.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 1.0 ],
            [ '2_2', 'T', 1.0 ],
            [ '2_3', 'T', 1.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 1.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 0.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 0.0 ],
            [ '2_2', 'F', 0.0 ],
            [ '2_3', 'F', 0.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 0.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 2_3
    stench_loc_2_3 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 1.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 1.0 ],
            [ '2_3', 'T', 1.0 ],
            [ '2_4', 'T', 1.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 1.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 0.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 0.0 ],
            [ '2_3', 'F', 0.0 ],
            [ '2_4', 'F', 0.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 0.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 2_4
    stench_loc_2_4 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 1.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 1.0 ],
            [ '2_4', 'T', 1.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 1.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 0.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 0.0 ],
            [ '2_4', 'F', 0.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 0.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 3_1
    stench_loc_3_1 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 1.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 1.0 ],
            [ '3_2', 'T', 1.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 1.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 0.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 0.0 ],
            [ '3_2', 'F', 0.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 0.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 3_2
    stench_loc_3_2 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 1.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 1.0 ],
            [ '3_2', 'T', 1.0 ],
            [ '3_3', 'T', 1.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 1.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 0.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 0.0 ],
            [ '3_2', 'F', 0.0 ],
            [ '3_3', 'F', 0.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 0.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 3_3
    stench_loc_3_3 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 1.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 1.0 ],
            [ '3_3', 'T', 1.0 ],
            [ '3_4', 'T', 1.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 1.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 0.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 0.0 ],
            [ '3_3', 'F', 0.0 ],
            [ '3_4', 'F', 0.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 0.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 3_4
    stench_loc_3_4 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 1.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 1.0 ],
            [ '3_4', 'T', 1.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 1.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 0.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 0.0 ],
            [ '3_4', 'F', 0.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 0.0 ]], [wumpus_loc_prob])


    # 4_1
    stench_loc_4_1 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 1.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 1.0 ],
            [ '4_2', 'T', 1.0 ],
            [ '4_3', 'T', 0.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 0.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 0.0 ],
            [ '4_2', 'F', 0.0 ],
            [ '4_3', 'F', 1.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 4_2
    stench_loc_4_2 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 1.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 1.0 ],
            [ '4_2', 'T', 1.0 ],
            [ '4_3', 'T', 1.0 ],
            [ '4_4', 'T', 0.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 0.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 0.0 ],
            [ '4_2', 'F', 0.0 ],
            [ '4_3', 'F', 0.0 ],
            [ '4_4', 'F', 1.0 ]], [wumpus_loc_prob])


    # 4_3
    stench_loc_4_3 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 1.0 ],
            [ '3_4', 'T', 0.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 1.0 ],
            [ '4_3', 'T', 1.0 ],
            [ '4_4', 'T', 1.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 0.0 ],
            [ '3_4', 'F', 1.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 0.0 ],
            [ '4_3', 'F', 0.0 ],
            [ '4_4', 'F', 0.0 ]], [wumpus_loc_prob])


    # 4_4
    stench_loc_4_4 = pomegranate.distributions.ConditionalProbabilityTable(
            [[ '1_2', 'T', 0.0 ],
            [ '1_3', 'T', 0.0 ],
            [ '1_4', 'T', 0.0 ],
            [ '2_1', 'T', 0.0 ],
            [ '2_2', 'T', 0.0 ],
            [ '2_3', 'T', 0.0 ],
            [ '2_4', 'T', 0.0 ],
            [ '3_1', 'T', 0.0 ],
            [ '3_2', 'T', 0.0 ],
            [ '3_3', 'T', 0.0 ],
            [ '3_4', 'T', 1.0 ],
            [ '4_1', 'T', 0.0 ],
            [ '4_2', 'T', 0.0 ],
            [ '4_3', 'T', 1.0 ],
            [ '4_4', 'T', 1.0 ],
            [ '1_2', 'F', 1.0 ],
            [ '1_3', 'F', 1.0 ],
            [ '1_4', 'F', 1.0 ],
            [ '2_1', 'F', 1.0 ],
            [ '2_2', 'F', 1.0 ],
            [ '2_3', 'F', 1.0 ],
            [ '2_4', 'F', 1.0 ],
            [ '3_1', 'F', 1.0 ],
            [ '3_2', 'F', 1.0 ],
            [ '3_3', 'F', 1.0 ],
            [ '3_4', 'F', 0.0 ],
            [ '4_1', 'F', 1.0 ],
            [ '4_2', 'F', 1.0 ],
            [ '4_3', 'F', 0.0 ],
            [ '4_4', 'F', 0.0 ]], [wumpus_loc_prob])

    # State objects hold both the distribution, and a high level name.
    wumpus_loc_prob_state = pomegranate.State(wumpus_loc_prob, name="wumpus_loc_prob")
    stench_loc_1_1_state = pomegranate.State(stench_loc_1_1, name="stench_loc_1_1")
    stench_loc_1_2_state = pomegranate.State(stench_loc_1_2, name="stench_loc_1_2")
    stench_loc_1_3_state = pomegranate.State(stench_loc_1_3, name="stench_loc_1_3")
    stench_loc_1_4_state = pomegranate.State(stench_loc_1_4, name="stench_loc_1_4")

    stench_loc_2_1_state = pomegranate.State(stench_loc_2_1, name="stench_loc_2_1")
    stench_loc_2_2_state = pomegranate.State(stench_loc_2_2, name="stench_loc_2_2")
    stench_loc_2_3_state = pomegranate.State(stench_loc_2_3, name="stench_loc_2_3")
    stench_loc_2_4_state = pomegranate.State(stench_loc_2_4, name="stench_loc_2_4")

    stench_loc_3_1_state = pomegranate.State(stench_loc_3_1, name="stench_loc_3_1")
    stench_loc_3_2_state = pomegranate.State(stench_loc_3_2, name="stench_loc_3_2")
    stench_loc_3_3_state = pomegranate.State(stench_loc_3_3, name="stench_loc_3_3")
    stench_loc_3_4_state = pomegranate.State(stench_loc_3_4, name="stench_loc_3_4")

    stench_loc_4_1_state = pomegranate.State(stench_loc_4_1, name="stench_loc_4_1")
    stench_loc_4_2_state = pomegranate.State(stench_loc_4_2, name="stench_loc_4_2")
    stench_loc_4_3_state = pomegranate.State(stench_loc_4_3, name="stench_loc_4_3")
    stench_loc_4_4_state = pomegranate.State(stench_loc_4_4, name="stench_loc_4_4")

    # Create the Bayesian network object with a useful name
    wumpus_model = pomegranate.BayesianNetwork("Wumpus Location")
    wumpus_model.add_states(wumpus_loc_prob_state, 
    stench_loc_1_1_state, stench_loc_1_2_state, stench_loc_1_3_state, stench_loc_1_4_state,
    stench_loc_2_1_state, stench_loc_2_2_state, stench_loc_2_3_state, stench_loc_2_4_state,
    stench_loc_3_1_state, stench_loc_3_2_state, stench_loc_3_3_state, stench_loc_3_4_state,
    stench_loc_4_1_state, stench_loc_4_2_state, stench_loc_4_3_state, stench_loc_4_4_state)

    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_1_1_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_1_2_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_1_3_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_1_4_state)

    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_2_1_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_2_2_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_2_3_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_2_4_state)

    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_3_1_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_3_2_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_3_3_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_3_4_state)

    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_4_1_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_4_2_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_4_3_state)
    wumpus_model.add_edge(wumpus_loc_prob_state, stench_loc_4_4_state)

    def __init__(self) -> None:
        pass 

    def bakeModel(self):
        self.wumpus_model.bake()

    def setWumpus_loc_prob(self, wup):
        self.wumpus_loc_prob = pomegranate.distributions.DiscreteDistribution(wup)
        self.wumpus_loc_prob_state = pomegranate.State(self.wumpus_loc_prob, name="wumpus_loc_prob")
        self.wumpus_model.add_states(self.wumpus_loc_prob_state, 
        self.stench_loc_1_1_state, self.stench_loc_1_2_state, self.stench_loc_1_3_state, self.stench_loc_1_4_state,
        self.stench_loc_2_1_state, self.stench_loc_2_2_state, self.stench_loc_2_3_state, self.stench_loc_2_4_state,
        self.stench_loc_3_1_state, self.stench_loc_3_2_state, self.stench_loc_3_3_state, self.stench_loc_3_4_state,
        self.stench_loc_4_1_state, self.stench_loc_4_2_state, self.stench_loc_4_3_state, self.stench_loc_4_4_state)

        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_1_1_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_1_2_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_1_3_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_1_4_state)

        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_2_1_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_2_2_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_2_3_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_2_4_state)

        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_3_1_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_3_2_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_3_3_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_3_4_state)

        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_4_1_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_4_2_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_4_3_state)
        self.wumpus_model.add_edge(self.wumpus_loc_prob_state, self.stench_loc_4_4_state)


print('Wumpus Stench Graph Built.')