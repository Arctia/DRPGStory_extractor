
mpath="C:/Users/Arctia/AppData/LocalLow/disgaearpg/DisgaeaRPG/assetbundle/masters/"
rpath="C:/Users/Arctia/Desktop/Root/Projects/DRPGStory/StoryFiles/masters/"

for VAR in "area" 'episode' 'event' 'story' 'storycharacter' 'storytalk'
do
	cp $mpath$VAR $rpath$VAR
	echo "$VAR copy was succesfull"
done

cd "StoryFiles"
echo "cd StoryFiles"

echo "py unpack.py"
py unpack.py

echo "cd .."
cd ..

echo "py excell.py"
py excell.py