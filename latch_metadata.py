from pathlib import Path

from latch.types.file import LatchFile
from latch.types.metadata import (LatchAuthor, SnakemakeFileParameter,
                                  SnakemakeMetadata)

SnakemakeMetadata(
    display_name="Snakemake Workflow: GATK best-practices",
    author=LatchAuthor(
        name="Johannes Koester",
    ),
    parameters={
        "samples_file": SnakemakeFileParameter(
            display_name="Samples TSV",
            type=LatchFile,
            path=Path("config/samples.tsv"),
        ),
        "units_file": SnakemakeFileParameter(
            display_name="Units TSV",
            type=LatchFile,
            path=Path("config/units.tsv"),
        ),
        "config_file": SnakemakeFileParameter(
            display_name="Config File",
            type=LatchFile,
            path=Path("config/config.yaml"),
        ),
        "known_variants": SnakemakeFileParameter(
            display_name="Known Variants (VCF File)",
            type=LatchFile,
            path=Path("data/known_variants.vcf"),
        ),
        "reads_1": SnakemakeFileParameter(
            display_name="Reads 1 FastQ",
            type=LatchFile,
            path=Path("data/reads.1.fq.gz"),
        ),
        "reads_2": SnakemakeFileParameter(
            display_name="Reads 2 FastQ",
            type=LatchFile,
            path=Path("data/reads.2.fq.gz"),
        ),
    },
)
