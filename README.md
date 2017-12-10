# gene2product
Curated list of gene names and product descriptions that pass NCBI genome submission rules. Used by funannotate during eukaryotic genome annotation.

I hope this is a "community" project where we can keep a list of gene names and their product definitions that pass NCBI requirements.  The `funannotate annotate` script will generate a list of gene names/product deflines that pass tbl2asn but are not in the database, to contribute you can do a PR of this repository.

1) Fork this repository
2) run `update-gene2product.py Gene2Products.new-names-passed.txt`
3) do a Pull Request with your update

#### Extra Credit:
`funannotate annotate` will also produce a file named `Gene2Products.need-curating.txt`, these are names/deflines that need manual curation.  If you manually curate these data, please validate that they pass tbl2asn prior to adding them to your PR.

Thanks!
