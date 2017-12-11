# gene2product
Curated list of gene names and product descriptions that pass NCBI genome submission rules. Used by funannotate during eukaryotic genome annotation.

I hope this is a "community" project where we can keep a list of gene names and their product definitions that pass NCBI requirements.  The `funannotate annotate` script will generate a list of gene names/product deflines that pass tbl2asn but are not in the database, to contribute you can do a PR of this repository.

1) Fork this repository
2) run `update-gene2product.py Gene2Products.new-names-passed.txt`
3) do a Pull Request with your update

#### Important:
While a product definition may pass tbl2asn, it doesn't mean that the description is *great*.  Please at least manually glance at the names/product deflines that are in the `Gene2Products.new-names-passed.txt` file prior to doing a PR, there are likely a few manual tweaks that can be quickly done to improve the product defline.

#### Extra Credit:
`funannotate annotate` will also produce a file named `Gene2Products.need-curating.txt`, these are names/deflines that need manual curation.  If you manually curate these data, please validate that they pass tbl2asn prior to adding them to your PR.

Thanks!
