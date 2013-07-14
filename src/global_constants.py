# some types have refittable capacity, they have to be known here currently (might change with migration from config file)
types_with_subtype_refits_for_capacity = ['log_tug', 'livestock_ship']
refittable_types_cargo_strings_buy_menu = {'log_tug':'STR_QUANTITY_WOOD', 'livestock_ship':'STR_QUANTITY_LIVESTOCK'}
refittable_types_cargo_strings_refit_menu = {'log_tug':'STR_UNIT_TONNES', 'livestock_ship':'STR_UNIT_ITEMS'}

purchase_list_sort_order = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 170, 210, 190, 200, 220, 230, 240, 250, 260, 270, 280, 290, 300]

# shared lists of allowed classes, shared across multiple ship types
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_EXPRESS', 'CC_ARMOURED', 'CC_BULK', 'CC_PIECE_GOODS', 'CC_LIQUID', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS','CC_ARMOURED','CC_EXPRESS','CC_LIQUID'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}


# used to construct the cargo table automatically
# stolen from BANDIT code which also offered option to specify random cargo variations - that part is not currently used in FISH
cargo_graphics_mappings = dict(AORE = [],
                               BDMT = [],
                               BEER = [],
                               CERE = [],
                               CLAY = [],
                               COAL = [],
                               COPR = [],
                               CORE = [],
                               DFLT = [],
                               DYES = [],
                               ENSP = [],
                               FICR = [],
                               FISH = [],
                               FMSP = [],
                               FOOD = [],
                               FRVG = [],
                               FRUT = [],
                               GOOD = [],
                               GRAI = [],
                               GRVL = [],
                               IORE = [],
                               LIME = [],
                               LVST = [],
                               MAIZ = [],
                               MILK = [],
                               MNSP = [],
                               OIL_ = [],
                               PASS = [],
                               PAPR = [],
                               PETR = [],
                               PLAS = [],
                               RFPR = [],
                               RUBR = [],
                               SAND = [],
                               SCMT = [],
                               SGBT = [],
                               SGCN = [],
                               STEL = [],
                               TOUR = [],
                               VEHI = [],
                               WATR = [],
                               WDPR = [],
                               WHEA = [],
                               WOOD = [],
                               WOOL = [])

# this is for nml, don't need to use python path module here
graphics_path = 'src/graphics/'

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# provide a private method for turning ships off during development without modifying the config file. Bound to go wrong. :P
ships_turned_off = (
)

