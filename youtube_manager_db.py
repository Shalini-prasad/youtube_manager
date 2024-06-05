import sqlite3
con = sqlite3.connect('youtube_videos.db')
cur = con.cursor()
cur.execute('''
  CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
  ) 
''')
def list_all_videos():
  cur.execute("SELECT * FROM videos")
  rows = cur.fetchall()
  for row in rows:
    print(list(row))
  

def add_video():
  name, time = video_detail_from_user()
  cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  con.commit()
  print("Video added successfully")

def update_video():
  video_id = input("Enter input id to update: ")
  name, time = video_detail_from_user()
  cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
  con.commit()
  print("Video updated successfully")
  

def delete_video():
  video_id = input("Enter video id to delete")
  cur.execute("DELETE from videos WHERE id = ?", (video_id,))
  con.commit()
  print("Video deleted successfully")
  

def video_detail_from_user():
  name = input("enter the video name: ")
  time = input("enter the video time: ")
  return name, time


def main():
  while True:
    print("\n Youtube manager app with DataBase")
    print("1. List Videos")
    print("2. Add Videos")
    print("3. Update Videos")
    print("4. Delete Videos")
    print("5. Exits App")

    choice = input("Enter your choice: ")

    match choice:
      case '1':
        list_all_videos()
      case '2':
        add_video()
      case '3':
        update_video()
      case '4':
        delete_video()
      case '5':
        break
      case _:
        print("Invalid Choice")




if __name__ == "__main__":
  main()
  con.close()

