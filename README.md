# gene2product
Curated list of gene names and product descriptions that pass NCBI genome submission rules. Used by fun annotate.

How to keep this file sorted:
```bash
(head -n 2 ncbi_cleaned_gene_products.txt && tail -n +3 ncbi_cleaned_gene_products.txt | sort) > ncbi_cleaned_gene_products.sorted.txt
```
