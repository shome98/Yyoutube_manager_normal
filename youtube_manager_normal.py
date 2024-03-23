import json

def load_data():
    try:
        with open('youtbe.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['duration']}")
    print("*"*70)

def add_video(videos):
    name=input("Enter the video name: ")
    time=input("Enter the video duration: ")
    videos.append({'name':name,'duration':time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update: "))
    if 1<=index<=len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video duration: ")
        videos[index-1]={'name':name,'duration':time}
        save_data(videos)
        print("Video updated successfully")
    else:
        print("Index does not exist!!!")
    
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data(videos)
        print("Video deleted successfully")
    else:
        print("Index does not exist!!!")
    pass

def main():
    videos=load_data()
    while True:
        print("This your youtube manager so please select an option")
        print("1. List all your youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice=input("Enter your option: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case '_':
                print("Enter a valid option")
if __name__=="__main__":
    main()

#this is just a basic cui with nomal add delete update display option every time the program runs even if the .txt file is there it gets overrided