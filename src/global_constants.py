# model lives are pretty standard, the game randomises them anyway so no need to offer much variety
model_lives = {
  'BANDIT_MODEL_LIFE_SHORT'  : 10,
  'BANDIT_MODEL_LIFE_MEDIUM' : 20,
  'BANDIT_MODEL_LIFE_LONG'   : 30,
}

# vehicles lives are pretty standard, not much gained by varying them in detail (although can add more options here if needed)
vehicle_lives = {
  'BANDIT_VEHICLE_LIFE_SHORT'  : 15,
  'BANDIT_VEHICLE_LIFE_MEDIUM' : 25,
  'BANDIT_VEHICLE_LIFE_LONG'   : 35,
}

# trucks refit to quite standard sets of cargos.  The main reason for variation is to provide gameplay difference between truck models
standard_class_refits = {
  'default' : {
        'allow'    : 'CC_MAIL, CC_EXPRESS, CC_ARMOURED, CC_BULK, CC_PIECE_GOODS, CC_LIQUID, CC_REFRIGERATED, CC_COVERED, CC_NON_POURABLE',
        'disallow' : 'CC_PASSENGERS',
  }
}

# body_types
class FifthWheelBT:
    def __init__(self, colourset_id):
        self.gestalt_id = 'body_fifth_wheel'
        self.colourset_id = colourset_id
        self.cargo = ''
        self.num_load_states = 1

class BoxBT:
    def __init__(self, colourset_id):
        self.gestalt_id = 'body_box'
        self.colourset_id = colourset_id
        self.cargo = ''
        self.num_load_states = 1

class FlatBT:
    def __init__(self, cargo, cargo_colourset_id):
        self.gestalt_id = 'body_flat'
        self.cargo = 'cargo_' + cargo
        self.cargo_colourset_id = cargo_colourset_id
        self.num_load_states = 5

class TankBT:
    def __init__(self, colourset_id):
        self.gestalt_id = 'body_tank'
        self.colourset_id = colourset_id
        self.cargo = ''
        self.num_load_states = 1

class TippingBT:
    def __init__(self, height_px, cargo_colourset_id):
        self.gestalt_id = 'body_tipping_' + height_px
        self.cargo = 'bulk'
        self.cargo_colourset_id = cargo_colourset_id
        self.num_load_states = 5



# use the dict constructor here, normally I don't, but it makes adding cargos faster (no string quotes needed).
# design note: small variations probably better than large ones, e.g. ['flat_large_crates','flat_small_crates'] rather than ['flat','tanker'].
# !! FlatBT('coils','white') indicates unfinished cargo support (except for paper)
fifth_wheel_body_type_mapping = dict(
    DFLT = [FifthWheelBT('blue_mask')], # special cases smell bad, but this is how I could think of to do it.
)
cargo_body_type_mappings = dict(
    AORE = [FlatBT('coils','white')],
    BDMT = [FlatBT('coils','white')],
    BEER = [FlatBT('coils','white'), TankBT('silver')],
    CERE = [TippingBT('4px','corn_yellow')],
    CLAY = [TippingBT('4px','clay_pink')],
    COAL = [TippingBT('4px','black')],
    COPR = [FlatBT('coils','white')],
    CORE = [FlatBT('coils','white')],
    DFLT = [BoxBT('cc1')],
    DYES = [TankBT('cc2')],
    ENSP = [FlatBT('coils','white')],
    FICR = [FlatBT('coils','white')],
    FISH = [BoxBT('cc1')],
    FMSP = [FlatBT('coils','white')],
    FOOD = [FlatBT('coils','white')],
    FRVG = [FlatBT('coils','white')],
    FRUT = [FlatBT('coils','white')],
    GOOD = [BoxBT('cc1')],
    GRAI = [TippingBT('4px','corn_yellow')],
    GRVL = [TippingBT('4px','grey')],
    IORE = [TippingBT('4px','iron_ore')],
    LIME = [TippingBT('4px','grey')],
    LVST = [FlatBT('coils','white')],
    MAIZ = [TippingBT('4px','corn_yellow')],
    MILK = [TankBT('silver')],
    MNSP = [FlatBT('coils','white')],
    OIL_ = [TankBT('black')],
    PAPR = [FlatBT('coils','white')],
    PETR = [TankBT('silver')],
    PLAS = [FlatBT('coils','white')],
    RFPR = [TankBT('cc2')],
    RUBR = [FlatBT('coils','white')],
    SAND = [TippingBT('4px','corn_yellow')],
    SCMT = [FlatBT('coils','white')],
    SGBT = [FlatBT('coils','white')],
    SGCN = [FlatBT('coils','white')],
    STEL = [FlatBT('coils','grey_metal')],
    VEHI = [FlatBT('coils','white')],
    WATR = [TankBT('cc1')],
    WDPR = [FlatBT('coils','white')],
    WHEA = [TippingBT('4px','corn_yellow')],
    WOOD = [FlatBT('coils','white')],
    WOOL = [FlatBT('coils','white')],
)

# needs to be deprecated; currently required by trucks
body_type_spritesheet_y_offset_mapping = dict (
    box          =  20,
)


# map truck weight factors to extra_type_info
cab_weight_factors = dict (
    local         = 0.8,
    line_haul     = 1,
    special_duty  = 0.8,
)
chassis_body_weight_factors = dict (
    local         = 0.8,
    line_haul     = 1,
    special_duty  = 1.2,
)

graphics_path = 'src/graphics/' # this is for nml, don't need to use python path module here
generated_images_path = 'src/pixel_generator/output/' # for nml, os.path not needed

# provide mapping of truck_type strings to numbers for use in range checks etc
# constants like this are one case where c pre-processor was a little more elegant than python
truck_type_nums = {
    'solo_truck'         : 0,
    'drawbar_truck'      : 1,
    'fifth_wheel_truck'  : 2,
}
# expose these identifiers as a convenience
solo_truck_type_num        = truck_type_nums['solo_truck']
fifth_wheel_truck_type_num = truck_type_nums['fifth_wheel_truck']
drawbar_truck_type_num     = truck_type_nums['drawbar_truck']

fifth_wheel_truck_quota = 0.5 # constant representing proportion of capacity etc transferred to fifth wheel trucks from first trailer

# provide a private method for turning vehicles off during development without modifying the config file. Bound to go wrong. :P
vehicles_turned_off = (
    'fayette_speedwagon',
    'hackler_AB',
    'hackler_BB',
    'hackler_CD',
    'latour_LT86',
    'latour_clipper',
    'pocomoke_wallman',
    'red_lake_cannonball',
    'red_lake_general',
    'reifsnider_281',
    'rothrock_CBE',
    'rothrock_R102',
    'rothrock_R123',
    'rothrock_rock_six',
    'rothrock_super',
    'wicomico_linkwood',
    'wicomico_northlander',
)
