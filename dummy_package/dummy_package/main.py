import sys
from dummy_package.classes.hello_world import HelloWorld

def main() -> None:
    hello_world_object: HelloWorld = HelloWorld()
    hello_world_object.print_first_words()
    hello_world_object.redefine_first_words(new_words="Hello World, Again!")
    hello_world_object.print_first_words()
    hello_world_object.define_more_words()
    print (hello_world_object.more_words)

if __name__ == '__main__':
    sys.exit(main())  # sys.exit takes either None or an int for exit code
    # main()  # This is also acceptable