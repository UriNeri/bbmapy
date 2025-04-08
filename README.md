# bbmapy

A Python wrapper for BBTools.

## Installation

```bash
conda install -c bioconda -c conda-forge bbmapy
```

## Usage

bbmapy let's you call bbtools stuff from python. To the shell only one CLI is available:  
- `bbmapy-test`: Run tests to verify installation

### Example

```python
from bbmapy import bbmap

# Run bbmap.sh
bbmap.bbmap(
    in1="reads1.fastq",
    in2="reads2.fastq",
    out="mapped.sam",
    ref="reference.fasta"
)
```

## Dependencies

- Python >= 3.9
- rich
- install-jdk (this will be used to install a JRE if needed)

## License
MIT
