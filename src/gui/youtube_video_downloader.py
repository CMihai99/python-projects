'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

font = ('verdana', 20)
file_size = 0

def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "Download Completed")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)

def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)

def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)
        file_size = st.filesize
        st.download(output_path=path_to_save)
    except Exception as e:
        print(e)
        print("something went wrong")

def btnClicked():
    try:
        downloadBtn['text'] = "Wait.."
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()
    except Exception as e:
        print(e)

# Main Window
root = Tk()
root.title("YouTube to MP4")
root.geometry("625x175")

# URL Field
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=15, pady=15)
urlField.focus()

# Download Video
downloadBtn = Button(root, text="Download MP4", font=font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=15)

# Run
root.mainloop()