from datetime import datetime
import keyboard
import pyimgur
import pyautogui
import pyperclip

# Text
print("#" * 57 + "\n\n   Press p to capture screen; any other key exits.   \n\n" + "#" * 57)

# Assuming imgur's client_id is in the first line of secrets.conf
with open('secrets.conf', 'r') as file:
    token = file.readline().replace('\n', '')

# Define time
time = str(datetime.now().strftime("%Y-%m-%d_%H%M%S"))

# Imgur upload using PyImgur
def imgur_upload():
    image_path = r"{}.png".format(time)
    im = pyimgur.Imgur(token)
    uploaded_image = im.upload_image(image_path, title="Uploaded with PyImgur")
    pyperclip.copy(uploaded_image.link)
    print("\n\nImage adress: " + uploaded_image.link)
    print("\n\nThe link has been copied to your clipboard.")

# App runs until p or any other key is pressed
while True:
    if keyboard.read_key() == "p":
        print("\nScreenshot saved as {}.png".format(time))
        screen = pyautogui.screenshot()
        screen.save(r"{}.png".format(time))
        imgur_upload()
        break
    else:
        print("Quit")
        break
