import pomegranate
import numpy

pit_1_2_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_1_3_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_1_4_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_2_1_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_2_2_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_2_3_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_2_4_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_3_1_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_3_2_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_3_3_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_3_4_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_4_1_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_4_2_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_4_3_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})
pit_4_4_prob = pomegranate.distributions.DiscreteDistribution({'T': 0.2, 'F': 0.8})

# 1_1
breeze_1_1_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]], [pit_1_2_prob, pit_2_1_prob])

# 1_2
breeze_1_2_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]],[pit_1_3_prob, pit_2_2_prob])

# 1_3
breeze_1_3_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]], [pit_1_2_prob, pit_1_4_prob, pit_2_3_prob])


# 1_4
breeze_1_4_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]], [pit_1_3_prob, pit_2_4_prob])

# 2_1
breeze_2_1_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]],[pit_2_2_prob, pit_3_1_prob])

# 2_2
breeze_2_2_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'F', 'T', 'F', 0.0 ],

         [ 'T', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'F', 1.0 ]], [pit_2_1_prob, pit_2_3_prob, pit_1_2_prob, pit_3_2_prob])

# 2_3
breeze_2_3_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'F', 'T', 'F', 0.0 ],

         [ 'T', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'F', 1.0 ]],[pit_2_2_prob, pit_2_4_prob, pit_1_3_prob, pit_3_3_prob])

# 2_4
breeze_2_4_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]],  [pit_2_3_prob, pit_1_4_prob, pit_3_4_prob])
    
# 3_1
breeze_3_1_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]], [pit_3_2_prob, pit_2_1_prob, pit_4_1_prob])

# 3_2
breeze_3_2_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'F', 'T', 'F', 0.0 ],

         [ 'T', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'F', 1.0 ]],[pit_3_1_prob, pit_3_3_prob, pit_2_2_prob, pit_4_2_prob])

# 3_3
breeze_3_3_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'F', 'T', 'F', 0.0 ],

         [ 'T', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 'F', 1.0 ]],[pit_3_2_prob, pit_3_4_prob, pit_2_3_prob, pit_4_3_prob])

# 3_4
breeze_3_4_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]],[pit_3_3_prob, pit_2_4_prob, pit_4_4_prob])

# 4_1
breeze_4_1_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]],[pit_4_2_prob, pit_3_1_prob])

# 4_2
breeze_4_2_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]], [pit_4_1_prob, pit_4_3_prob, pit_3_2_prob])

# 4_3
breeze_4_3_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 'T', 1.0 ],
         [ 'T', 'F', 'T', 'F', 0.0 ],
         [ 'F', 'T', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 'T', 1.0 ],
         [ 'F', 'F', 'T', 'F', 0.0 ],
         [ 'T', 'T', 'F', 'T', 1.0 ],
         [ 'T', 'T', 'F', 'F', 0.0 ],
         [ 'T', 'F', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'F', 'T', 1.0 ],
         [ 'F', 'T', 'F', 'F', 0.0 ],
         [ 'F', 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 'F', 1.0 ]],[pit_4_2_prob, pit_4_4_prob, pit_3_3_prob])

# 4_4
breeze_4_4_prob = pomegranate.distributions.ConditionalProbabilityTable(
        [[ 'T', 'T', 'T', 1.0 ],
         [ 'T', 'T', 'F', 0.0 ],
         [ 'T', 'F', 'T', 1.0 ],
         [ 'T', 'F', 'F', 0.0 ],
         [ 'F', 'T', 'T', 1.0 ],
         [ 'F', 'T', 'F', 0.0 ],
         [ 'F', 'F', 'T', 0.0 ],
         [ 'F', 'F', 'F', 1.0 ]], [pit_4_3_prob, pit_3_4_prob])

# State objects hold both the distribution, and a high level name.
pit_1_2_prob_state = pomegranate.State(pit_1_2_prob, name="pit_1_2_prob")
pit_1_3_prob_state = pomegranate.State(pit_1_3_prob, name="pit_1_3_prob")
pit_1_4_prob_state = pomegranate.State(pit_1_4_prob, name="pit_1_4_prob")

pit_2_1_prob_state = pomegranate.State(pit_2_1_prob, name="pit_2_1_prob")
pit_2_2_prob_state = pomegranate.State(pit_2_2_prob, name="pit_2_2_prob")
pit_2_3_prob_state = pomegranate.State(pit_2_3_prob, name="pit_2_3_prob")
pit_2_4_prob_state = pomegranate.State(pit_2_4_prob, name="pit_2_4_prob")

pit_3_1_prob_state = pomegranate.State(pit_3_1_prob, name="pit_3_1_prob")
pit_3_2_prob_state = pomegranate.State(pit_3_2_prob, name="pit_3_2_prob")
pit_3_3_prob_state = pomegranate.State(pit_3_3_prob, name="pit_3_3_prob")
pit_3_4_prob_state = pomegranate.State(pit_3_4_prob, name="pit_3_4_prob")

pit_4_1_prob_state = pomegranate.State(pit_4_1_prob, name="pit_4_1_prob")
pit_4_2_prob_state = pomegranate.State(pit_4_2_prob, name="pit_4_2_prob")
pit_4_3_prob_state = pomegranate.State(pit_4_3_prob, name="pit_4_3_prob")
pit_4_4_prob_state = pomegranate.State(pit_4_4_prob, name="pit_4_4_prob")

breeze_1_1_prob_state = pomegranate.State(breeze_1_1_prob, name="breeze_1_1_prob")
breeze_1_2_prob_state = pomegranate.State(breeze_1_2_prob, name="breeze_1_2_prob")
breeze_1_3_prob_state = pomegranate.State(breeze_1_3_prob, name="breeze_1_3_prob")
breeze_1_4_prob_state = pomegranate.State(breeze_1_4_prob, name="breeze_1_4_prob")

breeze_2_1_prob_state = pomegranate.State(breeze_2_1_prob, name="breeze_2_1_prob")
breeze_2_2_prob_state = pomegranate.State(breeze_2_2_prob, name="breeze_2_2_prob")
breeze_2_3_prob_state = pomegranate.State(breeze_2_3_prob, name="breeze_2_3_prob")
breeze_2_4_prob_state = pomegranate.State(breeze_2_4_prob, name="breeze_2_4_prob")

breeze_3_1_prob_state = pomegranate.State(breeze_3_1_prob, name="breeze_3_1_prob")
breeze_3_2_prob_state = pomegranate.State(breeze_3_2_prob, name="breeze_3_2_prob")
breeze_3_3_prob_state = pomegranate.State(breeze_3_3_prob, name="breeze_3_3_prob")
breeze_3_4_prob_state = pomegranate.State(breeze_3_4_prob, name="breeze_3_4_prob")

breeze_4_1_prob_state = pomegranate.State(breeze_4_1_prob, name="breeze_4_1_prob")
breeze_4_2_prob_state = pomegranate.State(breeze_4_2_prob, name="breeze_4_2_prob")
breeze_4_3_prob_state = pomegranate.State(breeze_4_3_prob, name="breeze_4_3_prob")
breeze_4_4_prob_state = pomegranate.State(breeze_4_4_prob, name="breeze_4_4_prob")

# Create the Bayesian network object with a useful name
pit_model = pomegranate.BayesianNetwork("Pit Location")
pit_model.add_states(pit_1_2_prob_state, pit_1_3_prob_state, pit_1_4_prob_state,
pit_2_1_prob_state, pit_2_2_prob_state, pit_2_3_prob_state, pit_2_4_prob_state,
pit_3_1_prob_state, pit_3_2_prob_state, pit_3_3_prob_state, pit_3_4_prob_state,
pit_4_1_prob_state, pit_4_2_prob_state, pit_4_3_prob_state, pit_4_4_prob_state,
breeze_1_1_prob_state, breeze_1_2_prob_state, breeze_1_3_prob_state, breeze_1_4_prob_state,
breeze_2_1_prob_state, breeze_2_2_prob_state, breeze_2_3_prob_state, breeze_2_4_prob_state,
breeze_3_1_prob_state, breeze_3_2_prob_state, breeze_3_3_prob_state, breeze_3_4_prob_state,
breeze_4_1_prob_state, breeze_4_2_prob_state, breeze_4_3_prob_state, breeze_4_4_prob_state)

pit_model.add_edge(pit_1_2_prob_state, breeze_1_1_prob_state)
pit_model.add_edge(pit_1_2_prob_state, breeze_2_2_prob_state)
pit_model.add_edge(pit_1_2_prob_state, breeze_1_3_prob_state)

pit_model.add_edge(pit_1_3_prob_state, breeze_1_2_prob_state)
pit_model.add_edge(pit_1_3_prob_state, breeze_1_4_prob_state)
pit_model.add_edge(pit_1_3_prob_state, breeze_2_3_prob_state)

pit_model.add_edge(pit_1_4_prob_state, breeze_1_3_prob_state)
pit_model.add_edge(pit_1_4_prob_state, breeze_2_4_prob_state)

pit_model.add_edge(pit_2_1_prob_state, breeze_2_2_prob_state)
pit_model.add_edge(pit_2_1_prob_state, breeze_1_1_prob_state)
pit_model.add_edge(pit_2_1_prob_state, breeze_3_1_prob_state)

pit_model.add_edge(pit_2_2_prob_state, breeze_2_1_prob_state)
pit_model.add_edge(pit_2_2_prob_state, breeze_2_3_prob_state)
pit_model.add_edge(pit_2_2_prob_state, breeze_1_2_prob_state)
pit_model.add_edge(pit_2_2_prob_state, breeze_3_2_prob_state)

pit_model.add_edge(pit_2_3_prob_state, breeze_2_2_prob_state)
pit_model.add_edge(pit_2_3_prob_state, breeze_2_4_prob_state)
pit_model.add_edge(pit_2_3_prob_state, breeze_1_3_prob_state)
pit_model.add_edge(pit_2_3_prob_state, breeze_3_3_prob_state)

pit_model.add_edge(pit_2_4_prob_state, breeze_2_3_prob_state)
pit_model.add_edge(pit_2_4_prob_state, breeze_1_4_prob_state)
pit_model.add_edge(pit_2_4_prob_state, breeze_3_4_prob_state)

pit_model.add_edge(pit_3_1_prob_state, breeze_3_2_prob_state)
pit_model.add_edge(pit_3_1_prob_state, breeze_2_1_prob_state)
pit_model.add_edge(pit_3_1_prob_state, breeze_4_1_prob_state)

pit_model.add_edge(pit_3_2_prob_state, breeze_3_1_prob_state)
pit_model.add_edge(pit_3_2_prob_state, breeze_3_3_prob_state)
pit_model.add_edge(pit_3_2_prob_state, breeze_2_2_prob_state)
pit_model.add_edge(pit_3_2_prob_state, breeze_4_2_prob_state)

pit_model.add_edge(pit_3_3_prob_state, breeze_3_2_prob_state)
pit_model.add_edge(pit_3_3_prob_state, breeze_3_4_prob_state)
pit_model.add_edge(pit_3_3_prob_state, breeze_2_3_prob_state)
pit_model.add_edge(pit_3_3_prob_state, breeze_4_3_prob_state)

pit_model.add_edge(pit_3_4_prob_state, breeze_3_3_prob_state)
pit_model.add_edge(pit_3_4_prob_state, breeze_2_4_prob_state)
pit_model.add_edge(pit_3_4_prob_state, breeze_4_4_prob_state)

pit_model.add_edge(pit_4_1_prob_state, breeze_4_2_prob_state)
pit_model.add_edge(pit_4_1_prob_state, breeze_3_1_prob_state)

pit_model.add_edge(pit_4_2_prob_state, breeze_4_1_prob_state)
pit_model.add_edge(pit_4_2_prob_state, breeze_4_3_prob_state)
pit_model.add_edge(pit_4_2_prob_state, breeze_3_2_prob_state)

pit_model.add_edge(pit_4_3_prob_state, breeze_4_2_prob_state)
pit_model.add_edge(pit_4_3_prob_state, breeze_4_4_prob_state)
pit_model.add_edge(pit_4_3_prob_state, breeze_3_3_prob_state)

pit_model.add_edge(pit_4_4_prob_state, breeze_4_3_prob_state)
pit_model.add_edge(pit_4_4_prob_state, breeze_3_4_prob_state)

pit_model.bake()

print("Pit Breeze Graph Built")