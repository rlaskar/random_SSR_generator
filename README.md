# Random SSR Generator

SSR & cSSR Focused Synthetic FASTA Generator

This script provides the ability to generate synthetic DNA sequences with a specific emphasis on Simple Sequence Repeats (SSRs) and Compound Simple Sequence Repeats (cSSRs).

## Description

The `random_SSR_generator.py` tool is tailor-made for bioinformatics applications demanding data simulation with a keen focus on SSRs and cSSRs. While the sequences it produces are synthetic and not derived from actual biological entities, they closely mirror genuine DNA sequences and include different types of SSRs, namely mono, di, tri, tetra, penta, and hexa repeats.

### Functional Highlights:

1. **Diverse SSR Generation**: The script can produce sequences containing diverse SSR types, from monomers to hexamers.
2. **cSSR Integration**: In addition to single SSRs, the generated sequences can also contain cSSRs – which are essentially two different SSRs juxtaposed next to each other.
3. **Random Sequence Inclusion**: Apart from the SSR and cSSR components, the script adds random DNA sequences for added variability, emulating the unpredictability found in real biological datasets.
4. **Configurable Output**: The script, by default, creates ten sequences, each 1000 base pairs long, but this can be easily customized.

### Output Format

The generated sequences are saved in the FASTA file format. Each sequence in the FASTA file starts with a descriptive line (preceded by the '>' symbol), followed by lines of sequence data. A default descriptor is utilized to indicate the sequence order in the file (e.g., '>synSeq_1' for the first sequence).

## Usage

### Prerequisites

- Ensure you have Python installed on your local system.

### Execution

1. Clone the repository:
```
git clone https://github.com/rlaskar/random_SSR_generator.git
cd [Repository Folder]
```

2. Run the script:
```
python random_SSR_generator.py
```

By default, the tool crafts ten sequences, each 1000 base pairs long, and saves them to `syntheticSequence_SSRcSSR.fasta`. If you wish to alter the number or length of sequences, you can tweak the parameters accordingly in the script.

## Customization

- Change `num_sequences` in the `save_sequences` function call to alter the number of sequences generated.
- Adjust the `sequence_length` parameter in the `generate_sequence` function to modify the length of each sequence.

```
