def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        #msg = "\nSorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + filename +
              " has about " + str(num_words) + " words.")


filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'love and peace.mobi',
             'moby_dick.txt', 'the art of art.pdf']
for filename in filenames:
    count_words(filename)
