WORLD     = u'\U0001F30E'
TELESCOPE = u'\U0001F52D'
ANTENNA   = u'\U0001F4E1'
SATELLITE = u'\U0001F6F0'

GREETING_TEXT = (""" Send me your location and i will reply with the next 5 visible Iridium flares in your area.
For more info on flares try /iridium,
For a glossary on location terms try /what
""")

HELP_STRING = ("""
/start - Send me your location to receive next flares
/iridium - Learn what causes an Iridium flare
/what - How to interpret the data provided by the bot
/help - Shows a helpful block of text

FAQ
-What is an Iridium Flare?
Try /iridium to learn more about satellite flares.

-I've got some feedback. How do i get in touch with you?
Contact me at @aBARICHELLO or try arturbarichello@hotmail.com

-How can i contribute?
https://www.github.com/abarichello/iridiumflarebot
""")

CONTRIBUTE_STRING = ("""
Contribute at: https://github.com/aBARICHELLO/IridiumFlarebot
""")

WHAT_STRING = ("""
Glossary:
*Altitude* - Angle between the horizon and the object in the sky (90º is the maximum, also called zenith)

*Azimuth* =
    _NORTH_ - 0º
    _EAST_  - 90º
    _SOUTH_ - 180º
    _WEST_  - 270º

*Brightness* - Brightness is expressed in aparent magnitude, the brighter an object appears,
the lower its magnitude value is.
Examples:
    _-26.30_ - Sun as seen from Earth
    _-12.90_ - Full Moon
    _-9.50_  - Maximum brightness of an Iridium flare
    _-4.89_  - Venus as seen from Earth
    _-2.50_  - New Moon
    _+1.84_  - Planet Mars
    _+5.95_  - Planet Uranus
    _+6.5_   - Starts that can be observed with the naked eye
    _+8.02_  - Planet Neptune
    _+9.50_  - Faintests objects visible using common 7x50 binnoculars

*Sun altitude* - The altitude of the sun in relation to the horizon. (Negative if sun is not visible)
""")

REMIND_MSG = (SATELLITE + " Iridium flare starting soon!")

USAGE_ERROR = ("Error. Usage example: /remindme 2017 Sep 12 10:02:45")

SECONDS_BEFORE = 600 # Seconds before event

SECONDS_MAX = 604800 # No further than a week

SUCESSFULL_TIME = ("""
Time set! You will be reminded 10 minutes before the next Iridium Flare
""")

IRIDIUM_STRING = ("""
The Iridium constellation with 66 active telecommunication
satellites in low Earth orbit are known to cause the brightest
flares of all orbiting satellites.
The Iridium communication satellites have a peculiar shape with
three polished door-sized antennas, 120° apart and at 40° angles
with the main bus. The forward antenna faces the direction
the satellite is travelling. """)

IRIDIUM_STRING2 = ("""Occasionally, an antenna reflects sunlight directly down at Earth,
creating a predictable and quickly moving illuminated spot on the
surface below of about 10 km (6.2 mi) diameter.
To an observer this looks like a bright flash, or flare in the sky, with a
duration of a few seconds.
""")

HEADER = "Here are the results for the next 7 days " + TELESCOPE

COLUMN = ['', 'Brightness: ', 'Altitude: ', 'Azimuth: ', 'Satellite: ', 'Distance to flare centre: ', 'Brightness at centre: ', 'Sun altitude: ']
