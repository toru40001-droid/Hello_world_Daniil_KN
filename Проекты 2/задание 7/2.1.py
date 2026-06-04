files = ["seq1", "seq2.fasta", "seq3.fa", "seq4"]
data = "12.03.2026"
for name in files:

    if name.endswith((".fasta", ".fa")):

        print(f"{name} уже имеет расширение")

    else:

        new_name = name + "." + data + ".fasta"

        print(f"{new_name}")