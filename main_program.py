# Class TV Exercise
# Getting the Function from the class_television
from class_television import Television

# Creating Objects
television_1 = Television()
television_2 = Television()

# Call the Instance Methods
television_1.turn_on()
television_2.turn_on()

television_1.set_channel(30)
television_2.set_channel(3)

television_1.set_volume(3)
television_2.set_volume(2)

# Display the Output
print("\ntv1's channel is", television_1.channel, "and volume level is", television_1.volume_level)
print("tv2's channel is", television_2.channel, "and volume level is", television_2.volume_level)

# Implementing other Instance Methods
television_1.channel_up()
television_2.volume_down()

print("\nSetting channel up and volume down:")
print("tv1's channel is", television_1.channel, "and volume level is", television_1.volume_level)
print("tv2's channel is", television_2.channel, "and volume level is", television_2.volume_level)

print("\nCurrent Channel and Volume:")
print("tv1's current channel is", television_1.get_channel(), "and current volume level is", television_1.get_volume())
print("tv2's current channel is", television_2.get_channel(), "and current volume level is", television_2.get_volume())

television_1.turn_off()
television_2.turn_off()

if television_1.on & television_2.on is False:
    print("\ntelevision 1 is now off")
    print("television 2 is now off")
