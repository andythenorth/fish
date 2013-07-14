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


# ! hangover code from BANDIT; can be used in future to match cargos to specific graphic variations
# also used to construct the cargo table automatically
# use the dict constructor here, normally I don't, but it makes adding cargos faster (no string quotes needed).
# design note: small variations probably better than large ones, e.g. ['flat_large_crates','flat_small_crates'] rather than ['flat','tanker'].
cargo_body_type_mappings = dict(AORE = [],
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

graphics_path = 'src/graphics/' # this is for nml, don't need to use python path module here
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# provide a private method for turning ships off during development without modifying the config file. Bound to go wrong. :P
ships_turned_off = (
)

