# Automatically Join Zoom Meetings With a Fake Virtual Feed

Annoyed with your daily meetings? Here's how to automatically join your meetings with a video feed on loop. 

## Step 1: Download OBS

You can follow the link below to setup OBS: https://github.com/CatxFish/obs-virtual-cam/releases

## Step 2: Change the camera of input for Zoom

Follow the steps here to do so. 

## Step 3: Clone this repository

Clone this repository. Go the project directory and run 
```
./build.sh 
```

### Step 4: In the folder itself, add a fake video feed. Call it 'VideoFeed.mp4'

### Step 5: Add your meetings

In scheduler.py, add your meetings to the list of meetings in the format 

`[<meeting_link,[list of days]>,time]`

Here, list of days include values [0,6]. 0 = Sunday, 1 = Monday and so on.  

### Step 6: Run automater
``` 
python MeetingAutomater.py
```

## Step 7: Sleep peacefully cause you don't have to attend your mundane meetings anymore. 

Here's a little demo for your reference!

![Demo](./res/Demo.gif)