from virus import Virus

def main():
    parent_virus = Virus("Parent", "SpeciesA", 1.5, 2)
    child_virus1 = Virus("Child1", "SpeciesA", 0.5, 1)
    child_virus2 = Virus("Child2", "SpeciesA", 0.6, 1)
    grandchild_virus = Virus("Grandchild", "SpeciesA", 0.3, 0.5)

    child_virus1.add_child(grandchild_virus)
    parent_virus.add_child(child_virus1)
    parent_virus.add_child(child_virus2)

    cloned_parent = parent_virus.clone()

    print(parent_virus)
    print(cloned_parent)

if __name__ == "__main__":
    main()
