# required libraries
from tkinter import *
from tkinter import messagebox
from pytube import YouTube, Playlist
import re, os
import time

# basic window
root = Tk()

# size in formate:- width x height
root.geometry("1000x500")
root.title("YouTube Downloader")

# minimum size in formate:- width, height
root.minsize(1000,500)

# maximum size in formate:- width, height
root.maxsize(1000,500)

# Download function 
def download():

    # user inputs
    user_link = linkvalue.get()
    user_path = pathvalue.get()

    # required inputs
    if user_link == "":
        messagebox.showinfo("Required","Enter link to download...")

    elif user_path == "":
        messagebox.showinfo("Required","Enter path to download...")

    # printing inputs
    print(f"link is: {user_link}")
    print(f"path is: {user_path}")

    # initialize folder name
    folder_name = "YouTube Downloader"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # download directory
    DOWNLOAD_DIR =  os.path.join(user_path, folder_name)
    print(DOWNLOAD_DIR)

    lst_regex = re.findall('^(https://youtube\.com/playlist\?list=){1}', user_link)

    # downloading playlist
    if lst_regex:
        try:    
            playlist = Playlist(user_link)
            for url in playlist.video_urls:
                yt = YouTube(url)
                print("Downloading...")
                yt.streams.get_highest_resolution().download(output_path=DOWNLOAD_DIR)
            messagebox.showinfo("Success",f"Downloaded video to this path {DOWNLOAD_DIR}")
        except Exception as e:
            raise Exception("Oops!! Something went wrong while downloading...")
    
    # download one single video
    else:
        try:
            yt = YouTube(user_link)
            print("Downloading...")
            download = yt.streams.get_highest_resolution().download(output_path=DOWNLOAD_DIR)
            messagebox.showinfo("Success",f"Downloaded video to this path {DOWNLOAD_DIR}")
        except Exception as e:
            print(e)
            raise Exception("Oops!! Something went wrong while downloading...")

# creating frames

# main frame
main_frame = Frame(root)
main_frame.pack(fill = "x")

# frame for Label 1
f_label1 = Frame(main_frame,borderwidth = 1,relief = "solid")
main_label = Label(f_label1, text="YouTube Downloader By Darshil Aslaliya", padx = 2, pady = 2,font="comicansms 16 bold")

# packing label 1
main_label.pack(fill = "x")
f_label1.pack(side = BOTTOM,anchor = "ne", fill = X)

#  frame for image
f2 = Frame(main_frame)
f2.pack(side = "top", anchor = "n", padx = 2, pady = 2)

# Logo 
photo = PhotoImage(file = "img/logo.png")
logo_img = Label(f2, image=photo)
logo_img.pack()

# for Label 2
f_label2 = Frame(main_frame)

linkvalue = StringVar()
pathvalue = StringVar()

# for link label and entry
Label(f_label2, text="Enter your Link here: ", padx = 2, pady = 15, font="comicansms 10 bold").grid()
link_entry = Entry(f_label2 ,textvariable = linkvalue, bd = 1, bg = "white", width=100)
link_entry.grid(row = 0, column = 1)

# for path label and entry
Label(f_label2, text="Enter your path here: ", padx = 2, pady = 15, font="comicansms 10 bold").grid(row = 1)
path_entry = Entry(f_label2, textvariable = pathvalue, bd = 1, bg = "white", width=100)
path_entry.grid(row = 1, column = 1)

# packing label 2
f_label2.pack(side = "top",anchor = "nw",padx = 112, pady = 10)

# frame for button
f3 = Frame(main_frame,borderwidth = 2,relief = "solid")
f3.pack(pady = 80)

# Download Button
download_btn = Button(f3, text = "Download", font="comicansms 18 bold",height = 40, width = 10, command = download)
download_btn.pack()

root.mainloop()