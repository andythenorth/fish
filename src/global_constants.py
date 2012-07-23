# vehicles refit to quite standard sets of cargos.  The main reason for variation is to provide gameplay difference between vehicle models
standard_class_refits = {
  'pax_mail_liquid_freight' : {
        'allow'    : 'CC_PASSENGERS, CC_MAIL, CC_EXPRESS, CC_ARMOURED, CC_BULK, CC_PIECE_GOODS, CC_LIQUID, CC_REFRIGERATED, CC_COVERED, CC_NON_POURABLE',
        'disallow' : '',
  },
  'liquid_freight' : {
        'allow'    : 'CC_EXPRESS, CC_ARMOURED, CC_BULK, CC_PIECE_GOODS, CC_LIQUID, CC_REFRIGERATED, CC_COVERED, CC_NON_POURABLE',
        'disallow' : 'CC_PASSENGERS, CC_MAIL',
  },
  'mail_liquid_freight' : {
        'allow'    : 'CC_MAIL, CC_EXPRESS, CC_ARMOURED, CC_BULK, CC_PIECE_GOODS, CC_LIQUID, CC_REFRIGERATED, CC_COVERED, CC_NON_POURABLE',
        'disallow' : 'CC_PASSENGERS',
  },
  'pax_mail' : {
        'allow'    : 'CC_PASSENGERS, CC_MAIL',
        'disallow' : 'CC_EXPRESS, CC_ARMOURED, CC_BULK, CC_PIECE_GOODS, CC_LIQUID, CC_REFRIGERATED, CC_COVERED, CC_NON_POURABLE',
  }
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

