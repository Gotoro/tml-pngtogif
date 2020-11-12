# tml-pngtogif
Transforms long sprite batch files into gifs.
![PNG](imgs/AkumuMirror.png)
![GIF](imgs/AkumuMirror.gif)

## Installation
Uses [Pillow](https://pillow.readthedocs.io/en/stable/index.html)
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
Was programmed in Python 3.7.3

## Usage
Place the image that you want to process in the same folder as the main.py

Open the command line in the same directory.

Type 
```python
python main.py IMAGE_NAME.png (optional)NUMBER_OF_FRAMES
```
The new gif should appear in the same directory under the same name as the image.

**Scripts determines the number of frames automatically. If it fails, you can always specify the NUMBER_OF_FRAMES yourself.**

For example, the image at the top has 7 frames, so to specify the number of frames do
```python
python main.py AkumuMirror.png 7
```
## Additional stuff
The script has commented line
```python
# region.save(regionname + str(i) + ".png")
```
Uncommenting it will make the script create, in addition to generating the gif, all the frames that it used.

For example, it will create 7 images AkumuMirror0-6.png for the example at the top. Useful if you want to extract the individual frames.
