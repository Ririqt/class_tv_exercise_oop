from class_television import Television

television_1 = Television()
television_2 = Television()

television_1.turn_on()
television_2.turn_on()

television_1.set_channel(30)
television_2.set_channel(3)

television_1.set_volume(3)
television_2.set_volume(2)

print("\ntv1's channel is", television_1.channel, "and volume level is", television_1.volume_level)
print("tv2's channel is", television_2.channel, "and volume level is", television_2.volume_level)

television_1.channel_up()
television_2.volume_down()
