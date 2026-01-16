import os 
import shlex
import subprocess


# Split 1 video into 3 parts: test - val - train
def split_video_to_test_val_train(input_directory, video_metadata, video_name, train_vid_path, val_vid_path, test_vid_path):
    """
    Split 1 video into 3 parts: test - val - train

    Parameters:
        input_directory (string): path to video folder
        video_metadata  (json)  : metadata of videos (i.e. data read from TSDOW_info.json)
        video_name      (string): name of splitted video
        train_vid_path  (string): path to video folder for train set
        val_vid_path    (string): path to video folder for val set
        test_vid_path   (string): path to video folder for test set
    
    Returns:
        A list of command to split videos.
    """

    data4video = {}
    video_id = video_name.split('.')[0]
    for data in video_metadata:
        if video_id == data["VIDEO_ID"]:
            data4video = data
            break 

    # print(video_id)
    video_duration = data4video["DURATION"]
    
    if video_duration > 480:
        # longer than 480s ~ 8mins
        # train <= 3 mins, val = 2 mins, test = 5 mins
        ffmpeg_train = "ffmpeg -ss 00:07:00 -to 00:10:00 -i " + input_directory + video_name + \
                   " -c copy " + train_vid_path + video_name
        ffmpeg_val   = "ffmpeg -ss 00:05:00 -to 00:07:00 -i " + input_directory + video_name + \
                    " -c copy " + val_vid_path + video_name
        ffmpeg_test  = "ffmpeg -ss 00:00:00 -to 00:05:00 -i " + input_directory + video_name + \
                    " -c copy " + test_vid_path + video_name
    elif video_duration > 360:
        # duration range: 6 mins (360s) - 8 mins (480s)
        # train <= 2.5 mins, val = 1.5 mins, test = 4 mins
        ffmpeg_train = "ffmpeg -ss 00:05:30 -to 00:08:00 -i " + input_directory + video_name + \
                   " -c copy " + train_vid_path + video_name
        ffmpeg_val   = "ffmpeg -ss 00:04:00 -to 00:05:30 -i " + input_directory + video_name + \
                    " -c copy " + val_vid_path + video_name
        ffmpeg_test  = "ffmpeg -ss 00:00:00 -to 00:04:00 -i " + input_directory + video_name + \
                    " -c copy " + test_vid_path + video_name
    else:
        # shortest video has duration: 00:04:55
        # train <= 2 mins, val = 1 mins, test = 3 mins
        ffmpeg_train = "ffmpeg -ss 00:04:00 -to 00:06:00 -i " + input_directory + video_name + \
                   " -c copy " + train_vid_path + video_name
        ffmpeg_val   = "ffmpeg -ss 00:03:00 -to 00:04:00 -i " + input_directory + video_name + \
                    " -c copy " + val_vid_path + video_name
        ffmpeg_test  = "ffmpeg -ss 00:00:00 -to 00:03:00 -i " + input_directory + video_name + \
                    " -c copy " + test_vid_path + video_name
    return [ffmpeg_train, ffmpeg_val, ffmpeg_test]


# Split all videos into 3 subsets: train, val, test
def split_videos_3_parts(input_directory, output_directory, video_metadata):
    """
    Split all videos into 3 subsets: train, val, test

    Parameters:
        input_directory     (string): path to raw videos (10 mins)
        output_directory    (string): path to dataset folder
        video_metadata      (json)  : metadata for videos in json format
    """
    TRAIN_PATH = output_directory + "train/";    os.makedirs(TRAIN_PATH, exist_ok=True)
    VAL_PATH = output_directory + "val/";        os.makedirs(VAL_PATH, exist_ok=True)
    TEST_PATH = output_directory + "test/";      os.makedirs(TEST_PATH, exist_ok=True)

    TRAIN_VIDEO_PATH = TRAIN_PATH + "videos/";  os.makedirs(TRAIN_VIDEO_PATH, exist_ok=True)
    VAL_VIDEO_PATH = VAL_PATH + "videos/";      os.makedirs(VAL_VIDEO_PATH, exist_ok=True)
    TEST_VIDEO_PATH = TEST_PATH + "videos/";    os.makedirs(TEST_VIDEO_PATH, exist_ok=True)

    all_items = os.listdir(input_directory)
    videos = []
    for item in all_items:
        if ".mp4" in item:
            videos.append(item)
    
    for video in videos:
        ffmpeg_train, ffmpeg_val, ffmpeg_test = split_video_to_test_val_train(input_directory, video_metadata, video, TRAIN_VIDEO_PATH, VAL_VIDEO_PATH, TEST_VIDEO_PATH)
        
        command_train = shlex.split(ffmpeg_train);  subprocess.run(command_train)
        command_val = shlex.split(ffmpeg_val);      subprocess.run(command_val)
        command_test = shlex.split(ffmpeg_test);    subprocess.run(command_test)