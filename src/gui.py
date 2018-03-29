from appJar import gui
import microbit

images = {
    'happy':"00000:09090:00900:90009:09990",
    'sad':"00000:09090:00900:09990:90009",
    'angry':"00000:09090:00900:99999:99999"
}

def pollButtons(name=None):
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed(): doButton("BOTH")
    elif microbit.button_a.is_pressed():  doButton("A")
    elif microbit.button_b.is_pressed():  doButton("B")

def pollPins():
    doPin(0, microbit.pin0.is_touched())
    doPin(1, microbit.pin1.is_touched())
    doPin(2, microbit.pin2.is_touched())

def pollSensors():
    accData = microbit.accelerometer.get_values()
    app.setStatusbar("X: "+str(accData[0]), 0)
    app.setStatusbar("Y: "+str(accData[1]), 1)
    app.setStatusbar("Z: "+str(accData[2]), 2)
    app.setStatusbar(str(microbit.temperature())+" c", 3)

def pollInputs():
    pollButtons()
    pollPins()
    pollSensors()
    app.after(200, pollInputs)

def doButton(name):
    print("Button %s", name)
    if name=="A": app.setMicroBitImage("mb1", images['happy'])
    elif name=="B": app.setMicroBitImage("mb1", images['sad'])
    elif name=="BOTH": app.setMicroBitImage("mb1", images['angry'])

def doPin(val, on=True):
    if on: app.label(str(val), bg="green")
    else:  app.label(str(val), bg="red")

with gui("bioio demo") as app:
    app.button("A", doButton, 1, 0)
    app.addMicroBit("mb1", 1, 1)
    app.button("B", doButton, 1, 2)
    with app.frame("pins", colspan=3):
        for i in range(3):
            app.label(str(i), sticky='news', relief='sunken', row=0, column=i)
    app.status(fields=4)
    app.after(50, pollInputs)
