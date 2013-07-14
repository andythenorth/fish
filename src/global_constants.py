# some types have refittable capacity, they have to be known here currently (might change with migration from config file)
types_with_subtype_refits_for_capacity = ['log_tug', 'livestock_ship']
refittable_types_cargo_strings_buy_menu = {'log_tug':'STR_QUANTITY_WOOD', 'livestock_ship':'STR_QUANTITY_LIVESTOCK'}
refittable_types_cargo_strings_refit_menu = {'log_tug':'STR_UNIT_TONNES', 'livestock_ship':'STR_UNIT_ITEMS'}

purchase_list_sort_order = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 170, 210, 190, 200, 220, 230, 240, 250, 260, 270, 280, 290, 300]

# types control strings and such, supertypes control refittability etc
type_supertype_mapping = {'hydrofoil_fast_ferry':'pax_mail',
                          'catamaran_fast_ferry':'packet',
                          'small_general_purpose_vessel':'trawler', # because it's similar to a packet, but needs to go fishing
                          'vehicle_ferry':'packet',
                          'paddle_steamer':'packet',
                          'fast_packet_steamer':'packet',
                          'cargo_vessel_inland':'gcv',
                          'log_tug':'log_tug',
                          'cargo_hovercraft':'fast_freighter',
                          'small_freighter_coastal_inland':'gcv',
                          'coaster':'gcv',
                          'large_coaster':'gcv',
                          'small_tanker_coastal_inland':'tanker',
                          'coastal_tanker':'tanker',
                          'large_coastal_tanker':'tanker',
                          'trawler':'trawler',
                          'livestock_ship':'livestock_ship',
                          'rig_supply_fast_catamaran':'packet',
                          'barge_tug':'gcv',
                          'container_feeder':'fast_freighter'}

# shared lists of allowed classes, may be shared by multiple supertypes
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_EXPRESS', 'CC_ARMOURED', 'CC_BULK', 'CC_PIECE_GOODS', 'CC_LIQUID', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS','CC_ARMOURED','CC_EXPRESS','CC_LIQUID'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# allowed labels, for fine-grained control in addition to classes
label_refits_allowed_by_supertype = {'gcv': [],
                                     'tanker': [],
                                     'pax_mail': [],
                                     'trawler': ['BDMT','FISH', 'FRUT','LVST','VEHI','WATR'], # trawler and packet are broadly similar
                                     'packet': ['BDMT','FRUT','LVST','VEHI','WATR'],
                                     'fast_freighter': ['FRUT','WATR'],
                                     'livestock_ship': ['LVST'], # set to livestock by default, don't need to make it refit
                                     'log_tug': []} # set to wood by default, don't need to make it refit

# allowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
label_refits_disallowed_by_supertype = {'gcv': ['TOUR'],
                                        'tanker': ['MILK'],
                                        'pax_mail': [],
                                        'trawler': [],
                                        'packet': ['FISH'],
                                        'fast_freighter': ['FISH','LVST','OIL_','TOUR','WOOD'],
                                        'livestock_ship': [],
                                        'log_tug': []}

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

