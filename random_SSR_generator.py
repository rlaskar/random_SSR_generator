#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def generate_ssr(ssr_type):
    """Generates a random SSR given the ssr_type (mono, di, tri, etc.)"""
    bases = 'ATGC'
    ssr_unit_length = {
        'mono': 1,
        'di': 2,
        'tri': 3,
        'tetra': 4,
        'penta': 5,
        'hexa': 6
    }
    # get random base(s) for SSR unit
    ssr_unit = ''.join(random.choice(bases) for _ in range(ssr_unit_length[ssr_type]))
    # decide a random repeat length for the SSR
    repeat_length = random.randint(3, 10)  # chosen range can be modified based on need
    return ssr_unit * repeat_length

def generate_sequence(sequence_length=1000):
    """Generates a random DNA sequence with a focus on SSRs and cSSRs"""
    sequence = ''
    while len(sequence) < sequence_length:
        # decide if next part is a random sequence, an SSR or a cSSR
        choice = random.choices(['random', 'ssr', 'cssr'], weights=[0.2, 0.4, 0.4], k=1)[0]
        if choice == 'random':
            rand_length = random.randint(10, 50)
            sequence += ''.join(random.choice('ATGC') for _ in range(rand_length))
        elif choice == 'ssr':
            ssr_type = random.choice(['mono', 'di', 'tri', 'tetra', 'penta', 'hexa'])
            sequence += generate_ssr(ssr_type)
        elif choice == 'cssr':
            ssr_type1 = random.choice(['mono', 'di', 'tri', 'tetra', 'penta', 'hexa'])
            ssr_type2 = random.choice(['mono', 'di', 'tri', 'tetra', 'penta', 'hexa'])
            sequence += generate_ssr(ssr_type1) + generate_ssr(ssr_type2)
    return sequence[:sequence_length]

def save_sequences(filename, num_sequences=10):
    with open(filename, 'w') as file:
        for i in range(num_sequences):
            sequence = generate_sequence()
            file.write(f'>synSeq_{i + 1}\n')
            file.write(sequence + '\n')

# Run the code to save the synthetic sequences
save_sequences('syntheticSequence_SSRcSSR.fasta')

