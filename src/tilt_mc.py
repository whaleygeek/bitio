import mcpi.minecraft as minecraft
import microbit
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    x = microbit.accelerometer.get_x()/300 # -ve=left/+ve=right
    y = microbit.accelerometer.get_y()/300 # -ve=forward/+ve=backward

    pos.x += x # east/west
    pos.z += y # north/south

    mc.player.setTilePos(pos.x, pos.y, pos.z)

    time.sleep(0.5)
