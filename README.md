# Random Battlezone Map Suggestion Bot
<img width="25%" src="./img/logo01.png">

Compatible with Discord.


## Features:
Choose maps by different query parameters like: `game=` `gamemode=` `bzn=` `mod=`


## Buckets:
Any bucket branch, `bucket`, can be updated aside from the `master` branch, to allocate map file resources, without affecting the codebase.

Eventually, mods can have their own designated bucket to open up more suggestions of playable maps available in Battlezone mods.

Each bucket will contain necessary `.bmp`s, `.des` and `.inf` data. Using a GitHub Actions pipeline, the bucket can be summarized into the bucket name's `.json` file. Raw data will be pulled from this "snapshot" to feed the live Bot.

## Getting started
1. Download `bucket-stock` branch with this command:
```
git clone -b bucket-stock https://github.com/BattlezoneScrapField/BZ-Map-Suggestion-Discord-Bot.git
```
2. Create and switch into a new branch.
3. Remove the provided example files in the corresponding folders.
4. Apply your changes and commit the branch.
