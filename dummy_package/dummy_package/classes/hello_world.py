class HelloWorld():
    def __init__(self, first_words_passed: str = "Hello World") -> None:
        super().__init__()

        self.first_words: str = first_words_passed

    def return_first_words(self) -> str:
        return self.first_words
    
    def print_first_words(self) -> None:
        print (self.return_first_words())

    def redefine_first_words(self, new_words: str) -> None:
        self.first_words = new_words
    
    def define_more_words(self) -> None:
        self.more_words: str = "I Love Python!"