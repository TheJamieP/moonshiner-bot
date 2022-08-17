"""
oooooo     oooo                     o8o             .o8       oooo
 `888.     .8'                      `"'            "888       `888
  `888.   .8'    .oooo.   oooo d8b oooo   .oooo.    888oooo.   888   .ooooo.   .oooo.o
   `888. .8'    `P  )88b  `888""8P `888  `P  )88b   d88' `88b  888  d88' `88b d88(  "8
    `888.8'      .oP"888   888      888   .oP"888   888   888  888  888ooo888 `"Y88b.
     `888'      d8(  888   888      888  d8(  888   888   888  888  888    .o o.  )88b
      `8'       `Y888""8o d888b    o888o `Y888""8o  `Y8bod8P' o888o `Y8bod8P' 8""888P'

"""
__EMBED_COLOUR__ = 0xFFFFFF
__prefix__ = "."
__BOT_MODE__ = "dev"

"""
oooooooooo.    o8o                .
`888'   `Y8b   `"'              .o8
 888      888 oooo   .ooooo.  .o888oo  .oooo.o
 888      888 `888  d88' `"Y8   888   d88(  "8
 888      888  888  888         888   `"Y88b.
 888     d88'  888  888   .o8   888 . o.)88b
o888bood8P'   o888o `Y8bod8P'   "888" 8""888P'
"""
bootleggar_recipe_costs = {
    # "categorys": [[water, alcohol, blackberry, raspberry, apple, creekplum, alaskan ginseng, american ginseng, peach, Hop, glass bottle]]
    "mash": [0.2, 0.32, 1, 1, 1, 1, 1, 1, 1, 1, 0.2],
    "alcohol": [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    "shine": {
        "blackberry": [0.2, 0.768, 3, 1],
        "raspberry": [0.2, 0.768, 3, 1],
        "apple": [0.2, 0.768, 3, 1],
        "creekplum": [0.2, 1.536, 3, 1],
        "alaskangin": [0.2, 1.536, 3, 1],
        "americangin": [0.2, 1.536, 3, 1],
        "peach": [0.2, 1.536, 3, 1],
        "moonshine": [0.2, 1.52, 2, 1],
        "blackberry90p": [0.2, 2.992, 2, 1],
        "raspberry90p": [0.2, 2.992, 2, 1],
    },
}

bootleggar_recipe_quantities = {
    # breakdown
    # "category":{
    #     "flavour": [array of quantities]
    # }
    "mash": {
        # "flavour": [water, alcohol, blackberry, raspberry, apple, creekplum, alaskan ginseng, american ginseng, peach, Hop, glass bottle]
        "blackberry": [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 5],
        "raspberry": [1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 5],
        "apple": [1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 5],
        "creekplum": [1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 5],
        "alaskangin": [1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 5],
        "americangin": [1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 5],
        "peach": [1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 5],
        "moonshine": [1, 5, 0, 0, 0, 0, 0, 0, 0, 1, 5],
        "blackberry90p": [1, 4, 5, 0, 0, 0, 0, 0, 0, 0, 5],
        "raspberry90p": [1, 4, 0, 5, 0, 0, 0, 0, 0, 0, 5],
    },
    "alcohol": [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    "shine": {
        "blackberry": [1, 1, 15, 1],
        "raspberry": [1, 1, 15, 1],
        "apple": [1, 1, 15, 1],
        "creekplum": [1, 2, 15, 1],
        "alaskangin": [1, 2, 15, 1],
        "americangin": [1, 2, 15, 1],
        "peach": [1, 2, 15, 1],
        "moonshine": [1, 2, 10, 1],
        "blackberry90p": [1, 2, 10, 1],
        "raspberry90p": [1, 2, 10, 1],
    },
}

farmer_seed_cost = {
    # name : price
    "indiantobacco": 0.35,
    "coffee": 0.2,
    "alaskanginseng": 0.15,
    "americanginseng": 0.15,
    "hop": 0.25,
    "blackberry": 0.2,
    "blackcurrant": 0.15,
    "bloodflower": 0.25,
    "chocdaisy": 0.2,
    "creekplum": 0.2,
    "creekingthyme": 0.2,
    "crowsgarlic": 0.2,
    "englishmace": 0.2,
    "milksage": 0.25,
    "oleandersage": 0.15,
    "oregano": 0.4,
    "parasolmushroom": 0.4,
    "priarepoppy": 0.5,
    "redraspberry": 0.25,
    "redsage": 0.2,
    "tea": 0.27,
    "wildcarrot": 0.15,
    "wildmint": 0.25,
    "wintergreenberry": 0.3,
    "yarrow": 0.25,
    "corn": 0.25,
    "apple": 0.3,
    "sugarcane": 0.2,
    "potato": 0.1,
    "cocoa": 0.35,
    "peach": 0.25,
}
