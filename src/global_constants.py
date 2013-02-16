# shared lists of allowed classes, may be shared by multiple supertypes
base_refits_by_class = {
    'empty': [],
    'all_freight': ['CC_EXPRESS', 'CC_ARMOURED', 'CC_BULK', 'CC_PIECE_GOODS', 'CC_LIQUID', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
    'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
    'liquids': ['CC_LIQUID'],
    'express_freight': ['CC_EXPRESS','CC_ARMOURED']
}
# mapping to lists of allowed classes.  No equivalent for disallowed classes, it's overly restrictive and damages the viability of class-based refitting
class_refit_groups_by_supertype = {
    'gcv': ['all_freight'],
    'tanker': ['liquids'],
    'pax_mail': ['pax_mail'],
    'trawler': ['pax_mail','express_freight'],
    'packet': ['pax_mail','express_freight'],
    'container_feeder': ['express_freight'],
    'livestock_ship': ['empty'],
    'log_tug': ['empty'],
}
# allowed labels, for fine-grained control in addition to classes
label_refits_allowed_by_supertype = {
    'gcv': [],
    'tanker': [],
    'pax_mail': [],
    'trawler': [],
    'packet': ['BDMT','LVST'],
    'container_feeder': [],
    'livestock_ship': [], # set to livestock by default, don't need to make it refit
    'log_tug': [], # set to wood by default, don't need to make it refit
}
# allowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
label_refits_disallowed_by_supertype = {
    'gcv': [],
    'tanker': [],
    'pax_mail': [],
    'trawler': [],
    'packet': ['FISH'],
    'container_feeder': [],
    'livestock_ship': [],
    'log_tug': [],
}

# ! hangover code from BANDIT; can be used in future to match cargos to specific graphic variations
# use the dict constructor here, normally I don't, but it makes adding cargos faster (no string quotes needed).
# design note: small variations probably better than large ones, e.g. ['flat_large_crates','flat_small_crates'] rather than ['flat','tanker'].
cargo_body_type_mappings = dict(
    AORE = [],
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
    VEHI = [],
    WATR = [],
    WDPR = [],
    WHEA = [],
    WOOD = [],
    WOOL = [],
)

graphics_path = 'src/graphics/' # this is for nml, don't need to use python path module here
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# provide a private method for turning vehicles off during development without modifying the config file. Bound to go wrong. :P
vehicles_turned_off = (
)

