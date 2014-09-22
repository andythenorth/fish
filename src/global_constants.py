
# shared lists of allowed classes, shared across multiple vehicle types
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
base_refits_by_class = {'empty': [],
                       'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                       'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
                       'liquids': ['CC_LIQUID'],
                       'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'refrigerated_freight': ['CC_REFRIGERATED'],
                       'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

label_refits_disallowed = {'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD'],
                           'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR']}

# used to construct the cargo table automatically
# stolen from BANDIT code which also offered option to specify random cargo variations - that part is not currently used in FISH
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
from ordered_dict_backport import OrderedDict
cargo_graphics_mappings = OrderedDict([('PASS', []), # pax first
                                       ('TOUR', []),
                                       # bulk-ish cargos
                                       ('COAL', []),
                                       ('IORE', []),
                                       ('GRVL', []),
                                       ('SAND', []),
                                       ('AORE', []),
                                       ('CORE', []),
                                       ('CLAY', []),
                                       ('SCMT', []),
                                       ('WOOD', []),
                                       ('LIME', []),
                                       # common express-ish / processed cargos
                                       ('GOOD', []),
                                       ('FOOD', []),
                                       ('STEL', []),
                                       ('FMSP', []),
                                       ('ENSP', []),
                                       ('BEER', []),
                                       ('BDMT', []),
                                       ('MNSP', []),
                                       ('PAPR', []),
                                       ('WDPR', []),
                                       ('VEHI', []),
                                       ('COPR', []),
                                       ('DYES', []),
                                       # liquid-ish cargos
                                       ('OIL_', []),
                                       ('RFPR', []),
                                       ('PETR', []),
                                       ('PLAS', []),
                                       ('WATR', []),
                                       # fish and farm cargos
                                       ('FISH', []),
                                       ('CERE', []),
                                       ('FICR', []),
                                       ('FRVG', []),
                                       ('FRUT', []),
                                       ('GRAI', []),
                                       ('LVST', []),
                                       ('MAIZ', []),
                                       ('MILK', []),
                                       ('RUBR', []),
                                       ('SGBT', []),
                                       ('SGCN', []),
                                       ('WHEA', []),
                                       ('WOOL', [])])

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = 'chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + '/graphics/'

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 740

# OpenTTD's max date
max_game_date = 5000001
