from cat.mutations import Mutations
from cat.cats import Cat

gen = Mutations()
cat = Cat()

genotype = gen.generate_genotype()



phenotype = gen.interpret_phenotype(genotype)

print(gen.get_mutation_dict(genotype, phenotype))


mutations = gen.get_mutation_dict(gen.init_mutations([cat.fetch_cat(i) for i in ("15", "16") if i]))
print(mutations)
