import random
from random import choice
from re import sub



class Mutations:


    def __init__(self):
        """self.ear_size_genes = None
        self.ear_type_genes = None
        self.eye_type_genes = None
        self.eye_count_genes = None
        self.tail_type_genes = None
        self.tail_count_genes = None
        self.teeth_genes = None
        self.horns_presence_genes = None
        self.horns_genes = None
        self.wings_presence_genes = None
        self.wings_type_genes = None
        self.wings_genes = None
        self.extras_presence_genes = None
        self.extras_genes = None"""

        self.ear_size_list = [
            "normal",
            "large",
            "small"
        ]

        self.ear_type_list = [
            "cat",
            "extra tuft",
            "rabbit",
            "dog",
            "no ears"
        ]

        self.eye_count_list = [
            2,
            3,
            8
        ]

        self.eye_type_list = [
            "cat",
            "abyss",
            "reptile",
            "goat",
            "frog",
            "compound"
        ]

        self.tail_type_list = [
            "cat",
            "squirrel",
            "rat",
            "devil",
            "dolphin"
        ]

        self.tail_count_list = [
            1,
            2,
            3
        ]

        self.teeth_list = [
            "cat",
            "fangs",
            "mandibles",
            "pedipalps"
        ]

        self.horns_presence_list = [
            False,
            True
        ]

        self.horns_list = [
            "goat",
            "deer",
            "ram",
            "antennae"
        ]

        self.wings_presence_list = [
            False,
            True
        ]

        self.wings_type_list = [
            "wyvern",
            "dragon"
        ]

        self.wings_list = [
            "bat",
            "bird",
            "insect",
            "pterosaur"
        ]

        self.extras_presence_list = [
            False,
            True
        ]

        self.extras_list = [
            "gills",
            "frills",
            "scales",
            "spines",
            "fins",
            "lure",
        ]

       


    def generate_genotype(self):
        """ generates the cats' mutations for cats without parents
        """
        ear_size_1 = random.choices(self.ear_size_list, weights=(50, 30, 20), k=1)[0]

        ear_type_1 = random.choices(self.ear_type_list, weights=(50, 25, 10, 10, 5), k=1)[0]

        eye_type_1 = random.choices(self.eye_type_list, weights=(50, 15, 15, 10, 5, 5), k=1)[0]

        eye_count_1 = random.choices(self.eye_count_list, weights=(90, 7, 3), k=1)[0]

        tail_type_1 = random.choices(self.tail_type_list, weights=(50, 15, 15, 10, 10), k=1)[0]

        tail_count_1 = random.choices(self.tail_count_list, weights=(90, 7, 3), k=1)[0]

        teeth_1 = random.choices(self.teeth_list, weights=(50, 20, 15, 15), k=1)[0]

        horns_presence_1 = random.choices(self.horns_presence_list, weights=(70, 30), k=1)[0]

        horns_1 = random.choices(self.horns_list, weights=(30, 30, 20, 20), k=1)[0]

        wings_presence_1 = random.choices(self.wings_presence_list, weights=(80, 20), k=1)[0]

        wings_type_1 = random.choices(self.wings_type_list, weights=(60, 40), k=1)[0]

        wings_1 = random.choices(self.wings_list, weights=(30, 30, 30, 10), k=1)[0]

        extras_presence_1 = random.choices(self.extras_presence_list, weights=(60, 40), k=1)[0]

        extras_1 = random.choices(self.extras_list, weights=(20, 40, 60, 80, 100, 120), k=1)

        ear_size_2 = random.choices(self.ear_size_list, weights=(50, 30, 20), k=1)[0]

        ear_type_2 = random.choices(self.ear_type_list, weights=(50, 25, 10, 10, 5), k=1)[0]

        eye_type_2 = random.choices(self.eye_type_list, weights=(50, 15, 15, 10, 5, 5), k=1)[0]

        eye_count_2 = random.choices(self.eye_count_list, weights=(90, 7, 3), k=1)[0]

        tail_type_2 = random.choices(self.tail_type_list, weights=(50, 15, 15, 10, 10), k=1)[0]

        tail_count_2 = random.choices(self.tail_count_list, weights=(90, 7, 3), k=1)[0]

        teeth_2 = random.choices(self.teeth_list, weights=(50, 20, 15, 15), k=1)[0]

        horns_presence_2 = random.choices(self.horns_presence_list, weights=(70, 30), k=1)[0]

        horns_2 = random.choices(self.horns_list, weights=(30, 30, 20, 20), k=1)[0]

        wings_presence_2 = random.choices(self.wings_presence_list, weights=(80, 20), k=1)[0]

        wings_type_2 = random.choices(self.wings_type_list, weights=(60, 40), k=1)[0]

        wings_2 = random.choices(self.wings_list, weights=(30, 30, 30, 10), k=1)[0]

        extras_presence_2 = random.choices(self.extras_presence_list, weights=(60, 30), k=1)[0]

        extras_2 = random.choices(self.extras_list, weights=(20, 40, 60, 80, 100, 120), k=1)[0]

        return {"ear_size": [ear_size_1, ear_size_2], 
                "ear_type": [ear_type_1, ear_type_2], 
                "eye_type": [eye_type_1, eye_type_2], 
                "eye_count": [eye_count_1, eye_count_2], 
                "tail_type": [tail_type_1, tail_type_2], 
                "tail_count": [tail_count_1, tail_count_2], 
                "teeth": [teeth_1, teeth_2], 
                "horns_presence": [horns_presence_1, horns_presence_2], 
                "horns": [horns_1, horns_2],
                "wings_presence": [wings_presence_1, wings_presence_2],
                "wings_type": [wings_type_1, wings_type_2],
                "wings": [wings_1, wings_2],
                "extras_presence": [extras_presence_1, extras_presence_2],
                "extras": [extras_1[0], extras_2]}


    def interpret_phenotype(self, genotype: dict):
        """
        get what mutations will be presenting from the genotype (list of two genes) given (meant to pair with generate_genotype)
        """
        self.ear_size = None
        self.ear_type = None
        self.eye_type = None
        self.eye_count = None
        self.tail_type = None
        self.tail_count = None
        self.teeth = None
        self.horns_presence = None
        self.horns = None
        self.wings_presence = None
        self.wings_type = None
        self.wings = None
        self.extras_presence = None
        self.extras = None

        i = 0
        while self.ear_size == None:
            if self.ear_size_list[i] == genotype["ear_size"][0] or self.ear_size_list[i] == genotype["ear_size"][1]:
                self.ear_size = self.ear_size_list[i]
            else:
                i += 1
        
        i = 0
        while self.ear_type == None:
            if self.ear_type_list[i] == genotype["ear_type"][0] or self.ear_type_list[i] == genotype["ear_type"][1]:
                self.ear_type = self.ear_type_list[i]
            else:
                i += 1
        
        i = 0
        while self.eye_type == None:
            if self.eye_type_list[i] == genotype["eye_type"][0] or self.eye_type_list[i] == genotype["eye_type"][1]:
                self.eye_type = self.eye_type_list[i]
            else:
                i += 1

        i = 0
        while self.eye_count == None:
            if self.eye_count_list[i] == genotype["eye_count"][0] or self.eye_count_list[i] == genotype["eye_count"][1]:
                self.eye_count = self.eye_count_list[i]
            else:
                i += 1

        i = 0
        while self.tail_type == None:
            if self.tail_type_list[i] == genotype["tail_type"][0] or self.tail_type_list[i] == genotype["tail_type"][1]:
                self.tail_type = self.tail_type_list[i]
            else:
                i += 1

        i = 0
        while self.tail_count == None:
            if self.tail_count_list[i] == genotype["tail_count"][0] or self.tail_count_list[i] == genotype["tail_count"][1]:
                self.tail_count = self.tail_count_list[i]
            else:
                i += 1

        i = 0
        while self.teeth == None:
            if self.teeth_list[i] == genotype["teeth"][0] or self.teeth_list[i] == genotype["teeth"][1]:
                self.teeth = self.teeth_list[i]
            else:
                i += 1

        i = 0
        while self.horns_presence == None:
            if self.horns_presence_list[i] == genotype["horns_presence"][0] or self.horns_presence_list[i] == genotype["horns_presence"][1]:
                self.horns_presence = self.horns_presence_list[i]
            else:
                i += 1

        if self.horns_presence == True:
            i = 0
            while self.horns == None:
                if self.horns_list[i] == genotype["horns"][0] or self.horns_list[i] == genotype["horns"][1]:
                    self.horns = self.horns_list[i]
                else:
                    i += 1
        
        i = 0
        while self.wings_presence == None:
            if self.wings_presence_list[i] == genotype["wings_presence"][0] or self.wings_presence_list[i] == genotype["wings_presence"][1]:
                self.wings_presence = self.wings_presence_list[i]
            else:
                i += 1

        if self.wings_presence == True:
            i = 0
            while self.wings_type == None:
                if self.wings_type_list[i] == genotype["wings_type"][0] or self.wings_type_list[i] == genotype["wings_type"][1]:
                    self.wings_type = self.wings_type_list[i]
                else:
                    i += 1

        if self.wings_presence == True:
            i = 0
            while self.wings == None:
                if self.wings_list[i] == genotype["wings"][0] or self.wings_list[i] == genotype["wings"][1]:
                    self.wings = self.wings_list[i]
                else:
                    i += 1

        i = 0
        if genotype["extras_presence"][0] == genotype["extras_presence"][1] == True:
            self.extras_presence = "two present"
        elif genotype["extras_presence"][0] == genotype["extras_presence"][1] == False:
            self.extras_presence = "none present"
        else:
            self.extras_presence = "one present"


        if self.extras_presence == "one present":
            i = 0
            while self.extras == None:

                if self.extras_list[i] == genotype["extras"][0] or self.extras_list[i] == genotype["extras"][1]:
                    self.extras = self.extras_list[i]
                else:
                    i += 1
        elif self.extras_presence == "two present":
            self.extras = genotype["extras"]
        


        return self.ear_size, self.ear_type, self.eye_type, self.eye_count, self.tail_type, self.tail_count, self.teeth, self.horns_presence, self.horns, self.wings_presence, self.wings_type, self.wings, self.extras_presence, self.extras
    
    def get_mutation_dict(self, genotype):
            self.phenotype = self.interpret_phenotype(genotype)
            
            ear_size_genes = [self.ear_size, [genotype["ear_size"][0], genotype["ear_size"][1]]]
            ear_type_genes = [self.ear_type, [genotype["ear_type"][0], genotype["ear_type"][1]]]
            eye_type_genes = [self.ear_type, [genotype["eye_type"][0], genotype["eye_type"][1]]]
            eye_count_genes = [self.eye_count, [genotype["eye_count"][0], genotype["eye_count"][1]]]
            tail_type_genes = [self.tail_type, [genotype["tail_type"][0], genotype["tail_type"][1]]]
            tail_count_genes = [self.tail_count, [genotype["tail_count"][0], genotype["tail_count"][1]]]
            teeth_genes = [self.teeth, [genotype["teeth"][0], genotype["teeth"][1]]]
            horns_presence_genes = [self.horns_presence, [genotype["horns_presence"][0], genotype["horns_presence"][1]]]
            horns_genes = [self.horns, [genotype["horns"][0], genotype["horns"][1]]]
            wings_presence_genes = [self.wings_presence, [genotype["wings_presence"][0], genotype["wings_presence"][1]]]
            wings_type_genes = [self.wings_type, [genotype["wings_type"][0], genotype["wings_type"][1]]]
            wings_genes = [self.wings, [genotype["wings"][0], genotype["wings"][1]]]
            extras_presence_genes = [self.extras_presence, [genotype["extras_presence"][0], genotype["extras_presence"][1]]]
            extras_genes = [self.extras, [genotype["extras"][0], genotype["extras"][1]]]
            
            return ear_size_genes, ear_type_genes, eye_type_genes, eye_count_genes, tail_type_genes, tail_count_genes, teeth_genes, horns_presence_genes, horns_genes, wings_presence_genes, wings_type_genes, wings_genes, extras_presence_genes, extras_genes
    

    
    def init_mutations(self):
        mutations = Mutations()
        self.genotype = mutations.generate_genotype()
        #print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        
        """if not parents:
            self.genotype = mutations.generate_genotype()
        else:
            self.genotype = {}
            print(parents)
            e = parents[0]
            #i = parents[0].mutations.ear_size_genes

            #print(f'i: {i}')
            #print(f'e: {e}')
            #print(type(e))
            i = set()
            i.add(e.mutations.ear_type_genes)
            print(i)
            self.genotype["ear_size"] = random.choice(i[1])
            self.genotype["ear_type"] = random.choice(i["ear_type"])
            self.genotype["eye_type"] = random.choice(i["eye_type"])
            self.genotype["eye_count"] = random.choice(i["eye_count"])
            self.genotype["tail_type"] = random.choice(i["tail_type"])
            self.genotype["tail_count"] = random.choice(i["tail_count"])
            self.genotype["teeth"] = random.choice(i["teeth"])
            self.genotype["horns_presence"] = random.choice(i["horns_presence"])
            self.genotype["horns"] = random.choice(i["horns"])
            self.genotype["wings_presence"] = random.choice(i["wings_presence"])
            self.genotype["wings_type"] = random.choice(i["wings_type"])
            self.genotype["wings"] = random.choice(i["wings"])
            self.genotype["extras_presence"] = random.choice(i["extras_presence"])
            self.genotype["extras"] = random.choice(i["extras"])

            j = parents[1].mutations.get_mutation_dict
            self.genotype["ear_size"].append(random.choice(j["ear_size"]))
            self.genotype["ear_type"].append(random.choice(j["ear_type"]))
            self.genotype["eye_type"].append(random.choice(j["eye_type"]))
            self.genotype["eye_count"].append(random.choice(j["eye_count"]))
            self.genotype["tail_type"].append(random.choice(random.choice(j["tail_type"])))
            self.genotype["tail_count"].append(random.choice(j["tail_count"]))
            self.genotype["teeth"].append(random.choice(j["teeth"]))
            self.genotype["horns_presence"].append(random.choice(j["horns_presence"]))
            self.genotype["horns"].append(random.choice(j["horns"]))
            self.genotype["wings_presence"].append(random.choice(j["wings_presence"]))
            self.genotype["wings_type"].append(random.choice(j["wings_type"]))
            self.genotype["wings"].append(random.choice(j["wings"]))
            self.genotype["extras_presence"].append(random.choice(j["extras_presence"]))
            self.genotype["extras"].append(random.choice(j["extras"]))

        return self.genotype"""

        