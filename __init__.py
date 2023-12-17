from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import
from .Locations import
from .Regions import
from .Options import sky_options
from .Presets import sky_options_presets
from .Rules import


class SkyrimWeb(WebWorld):
    theme = "stone"
    setup = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Skyrim randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Sekomura"]
    )]
    bug_report_page = "https://github.com/Sekomura/SkyrimRandomizer/issues/new"
    options_presets = sky_options_presets

    class SkyrimWorld(World):
        """
        The titular The Elder Scrolls V: Skyrim is a open world fantasy role-playing game made in 2011.
        Play as the Dragonborn, a humanoid being with the sould of a dragon, and save the realm of Skyrim and all of Tamriel from the World Eater, Alduin.
        """
      
      game: = "Skyrim"
      topology_present = 
      data_version =  
      required_client_version =  
      web = SkyrimWeb()
