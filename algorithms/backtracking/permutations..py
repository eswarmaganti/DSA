from typing import List


class Permutate:

    def __init__(self, elements: List[str]) -> None:
        self.elements: List[str] = elements
        self.results: List[List[str]] = []

    def get_permutations(self) -> List[List[str]]:
        self.backtrack(current=[], options=self.elements)
        return  self.results

    def backtrack(self,current: List[str], options: List[str]) -> None:
        if len(current) == len(self.elements):
            self.results.append(current)
        else:

            for index, choice in enumerate(options):
                self.backtrack(current=current+[choice], options=options[:index]+options[index+1:])


if __name__ == "__main__":
    elements: List[str] = input("Enter elements as comma separated values: ").split(",")
    obj = Permutate(elements)

    print("The all possible combinations are: ")
    print(obj.get_permutations())