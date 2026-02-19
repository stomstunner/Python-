# here we make a project where we can manage the youtube videos, we can add the yt videos and delte and update a list


# import json
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# FILE_PATH = os.path.join(BASE_DIR, "youtube.txt")

# def load_data():
#     try:
#         with open(FILE_PATH, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []

# def save_data_helper(videos):
#     with open(FILE_PATH, 'w') as file:
#         json.dump(videos, file)



import json

# here we make a defination where we load our file data from file and convert the string to a json formate (javascript object notation)
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)   
    except FileNotFoundError:
        return []

#here we make a helper methods that help us to save the new or updated youtubr videos

def sava_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        # jeson dump method recive 2 thing 1 is  what to dump and 2nd is where to dump
        
# lets make the defination for all the features
def list_all_videos(videos):
    # now we write a code for changing the list to a enumurate
    # now we write the code for formatting
    print("\n") 
    print("."*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n") 
    print("."*50)


def add_videos(videos):
    # now we take the input from the user name and timing
    name = input("Enter the video name: ")
    time = input("Enter the length of the video: ")
            # now we append the name and videos time in the list like a aray of array or we can say a dist
            # ({"name":name,"time":time})
    videos.append({'name': name, 'time': time})
            # now we save the data with the help of helper defination
    sava_data_helper(videos)


def update_videos(videos):
    # here we give the all the list of the videos to the user so the user can tell me which ranked number item/video thery want to update
    list_all_videos(videos)
    index = int(input("Enter the video that you want to Update: "))
    # now we create a if statement that check that hamra video number 1 se bar aur video ki list ke lenght se  chota ho
    if 1 <= index <= len(videos):
        name = input("Enter the name of the video: ")
        time = input("Enter the time of the video: ")
        videos[index-1] = {'name':name, 'time':time}
        sava_data_helper(videos)
    else:
        print("Invalid Index Selected!")
        


def delete_videos(videos):
    # now we write the code for delition of selected video detail
    list_all_videos(videos)
    index = int(input("Enter the video number that you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        sava_data_helper(videos)
        print("Delition Successfull!")
    else:
        print("Invlaid Index Selected!")
        

def main():
    videos = load_data()
                    # first of we make a options where we  can give the options to the user so they can select the one opetion at a time but that option ware run in a infinite loop so we write it in the while loop
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all Youtube Videos ")
        print("2. Add a Youtube Videos ")
        print("3. Update a Youtube Videos details ")
        print("4. Delete a Youtube Videos ")
        print("5. Exit the app ")
        choice = input("\nEnter Your Choice: ")
        # print(videos)

        # now we have a new method just like the switch statement
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
        # now in place of default we use just a underscore
            case _:
                print("Invalid Choice")
                
# now we have a starting point of the file i.e, main() jisko ki hame call karne ke liye ham yahi proper syntax use karnege
# woh underscore underscore wale function ko ham dunder kahate hau

if __name__ == "__main__":
    main()
# iska saaf matlab hai ki ager kahi bhi file me deination ka naam main hoga toh usse chala denna
