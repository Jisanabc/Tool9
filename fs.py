import os
import time

def search_file(file_name):
    results = []
    for root, dirs, files in os.walk(os.getcwd()):
        if file_name in files:
            results.append(os.path.join(root, file_name))
    return results

def display_logo():
    logo = "######## JX-FILE ########"
    print("\033[1;32;40m" + logo.center(os.get_terminal_size().columns) + "\033[0m")

def display_file_location(location):
    print("\033[1;31;40m" + location + "\033[0m")

def search_animation():
    animation_frames = ["Searching.", "Searching..", "Searching..."]
    for frame in animation_frames:
        print(frame, end="", flush=True)
        time.sleep(0.5)
        print("\r", end="", flush=True)

def main():
    display_logo()
    print("Enter file name: ", end="")
    user_input = input()
    
    print("\nSearching for the file. Please wait.")
    search_animation()
    
    results = search_file(user_input)
    
    if results:
        print("\nFile found at the following location(s):")
        for result in results:
            display_file_location(result)
    else:
        print("\nFile not found.")

if __name__ == "__main__":
    main()