import mcpi.minecraft as minecraft
import microbit
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    x = microbit.accelerometer.get_x()/300
    y = microbit.accelerometer.get_y()/300

    pos.x += x
    pos.y += y

    mc.player.setTilePos(x, y, pos.z)

    time.sleep(0.5)
