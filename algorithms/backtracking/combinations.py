from typing import List

# Combinations Class


class Combination:

    def __init__(self, elements: List[str], size: int) -> None:
        self.elements: List[str] = elements
        self.size: int = size
        self.results: List[List[str]] = []

    def generate_combinations(self)-> List[List[str]]:
        self.backtrack(current=[], options=self.elements, size=self.size)
        return self.results

    def backtrack(self,current: List[str],options: List[str], size: int):
        if size == 0:
            self.results.append(current)
        else:
            for index, choice in enumerate(options):
                self.backtrack(current=current+[choice], options=options[index+1:], size=size-1 )


if __name__ == "__main__":
    elements = input("Enter the elements as comma separated values: ").split(",")
    size = int(input("Enter the size of combinations to generate: "))
    obj = Combination(elements,size)

    print(f"The possible combinations of size - {size} are: ")
    print(obj.generate_combinations())