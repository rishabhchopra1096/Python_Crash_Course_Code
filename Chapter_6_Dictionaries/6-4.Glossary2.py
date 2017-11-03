glossary = {
    'print':'Prints the data struture followed after the print statement.',
    'range':'Creates a list of numbers starting from the first' +
    'number till the last number - 1.\nYou can also add interval.',
    'sort()':'This method sorts the list in alphabetical order , permanently.',
    'del':'Deletes an item/key-value pair in a list/dictionary respectively.',
    'insert':'Inserts an element into the list at the mentioned index number.',
    'remove':'Allows you to remove items from a list while having access to them.',
    '.items':'Creates a list of tuples. Each tuple consist of one key-value pair.' +
    "\ndic.items() = [('key1','value1'),('key2','value2')]",
    '.keys()':'Create a tuple with a list of all keys in the dictionary.',
    '.values()':'Creates a tuple with a list of all values in the dictionary.',
}



for function , meaning in glossary.items():
    print(function + ":\n\t" + meaning)

