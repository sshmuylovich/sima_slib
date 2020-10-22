
> How do I test that the letters in a word are either next to each other or diagonal on a grid without going through the same grid location more than once?

You could use a recursive 2d depth first search algorithm! Check out [this site](https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/) for more info. If the runtime for checking each word against the dictionary using the Merriam Webster API turns out to be too long, you can use a prefix tree to search. This is a much faster solution, but would take a little longer to implement if you haven't seen it before. 

