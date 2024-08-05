import requests

class Compound:
    def __init__(self, title, molecular_formula, molecular_weight) :
        self.title = title
        self.molecular_formula = molecular_formula
        self.molecular_weight = molecular_weight
    
    def __str__(self):
        return (f"Name: {self.title}\n"
                f"Molecular Formula: {self.molecular_formula}\n"
                f"Molecular Weight: {self.molecular_weight}\n")

def get_compound_info(cid):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    endpoint = f"/compound/cid/{cid}/property/Title,MolecularFormula,MolecularWeight/JSON"
    url = base_url+endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        properties = data["PropertyTable"]["Properties"][0]

        return Compound(
            title= properties.get('Title'),
            molecular_formula=properties.get('MolecularFormula'),
            molecular_weight=properties.get('MolecularWeight')
        )
    except requests.exceptions.HTTPError:
        print(f"Invalid CID number\n")
        return None


def get_cid_byCAS(cas):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    endpoint = f"/compound/name/{cas}/cids/JSON"
    url = base_url+endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        cid = data["IdentifierList"]["CID"][0]
        return cid
    
    except requests.exceptions.HTTPError:
        print(f"Invalid CAS number\n")
        return None
    
def get_cid_byname(string):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    endpoint = f"/compound/name/{string}/cids/JSON"
    url = base_url+endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        cid = data["IdentifierList"]["CID"][0]
        return cid
    
    except requests.exceptions.HTTPError:
        print(f"Invalid name\n")
        return None


def main():
    while True:
        try:
            choice = input("Get compound information by (input number only):\n 1 CID\n 2 CAS\n 3 Name\n")

            if choice == "1":
                cid = input("Input CID number here: ").strip()
                compound_info = get_compound_info(cid)
                if compound_info:
                    print(compound_info)

            elif choice == "2":
                cas = input("Input CAS number here: ").strip()
                cid = get_cid_byCAS(cas)
                if cid:
                    print(f"Here is the corresponding CID: {cid}")
                    compound_info = get_compound_info(cid)
                    print(compound_info)

            elif choice == "3":
                name = input("Input compound's name here: ").strip()
                cid = get_cid_byname(name)
                if cid:
                    print(f"Here is the corresponding CID: {cid}")
                    compound_info = get_compound_info(cid)
                    print(compound_info)
            else:
                print(f"Invalid input, please select again.")

        except EOFError:
            print("The program has been closed.")
            break

if __name__ == "__main__":
    main()