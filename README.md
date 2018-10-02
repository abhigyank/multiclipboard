# multiclipboard
Say you have the boring task of filling out many forms in a web page or software with several text fields. The clipboard saves you from typing the same text over and over again. But only one thing can be on the clipboard at a time. If you have several different pieces of text that you need to copy and paste, you have to keep highlighting and copying the same few things over and over again.
Multiclipboard helps to maintain multiple clipboards under unique keywords which reduces the work of copying different stuff again and again.
This is a Python program to keep track of multiple pieces of text. This “multiclipboard” is named mcb.py.

Usage- 
- Place the `mcb.bat` and `mcb.py` file in a same folder, preferably `C:\Users\*username*\`
- Run the mcb.bat file from the run window (windows+r r launch the run window and execute `C:\Users\*username*\mcb.bat`
- Put the required keyword/keywords after .bat followed by a space 

Keywords-
- `mcb.bat save <keyword>` - Saves content on original clipboard to keyword, SELECT THE REQUIRED TEXT TO BE COPIED TO KEYWORD AND PRESS CTRL+C TO FIRST COPY IT TO ORIGINAL CLIPBOARD 
- `mcb.bat <keyword>` - Loads the content saved in keyword to clipboard, press ctrl+ v to paste the content.
- `mcb.bat list` - Lists all keywords saved till then.
- `mcb.bat delete <keyword>` - Deletes the keyword and its content
- `mcb.bat delete all` - Deletes all the keywords and their contents

#### Example command to save - 
`C:\Users\*username*\mcb.bat save clip`

^This will save the text on the original clipboard to clip keyword.
