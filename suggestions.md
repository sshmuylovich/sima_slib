
> How do I test that the letters in a word are either next to each other or diagonal on a grid without going through the same grid location more than once?

You could use a recursive 2d depth first search algorithm! Check out [this site](https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/) for more info. If the runtime for checking each word against the dictionary using the Merriam Webster API turns out to be too long, you can use a prefix tree to search. This is a much faster solution, but would take a little longer to implement if you haven't seen it before. 

> How to set a default font for the Tkinter Graphic User Interface (GUI) 
1) You can use one of the built in Tkinter fonts such as TkDefaultFont, TkTextFont, TkFixedFont. 
2) Get a handle of the font and then use the ```python configure ``` method to alter the size of the font as shown below
```python
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=48)
```
3) To add this default font to all your widgets, use 
```python 
root.option_add("*Font", default_font)
```
NOTE: For ```python option_add``` to be present in all files, classes, and widgets, you must only implement it BEFORE creating widgets

Sources/Citations: 
https://stackoverflow.com/questions/15462647/modify-the-default-font-in-python-tkinter
