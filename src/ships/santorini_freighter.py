from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'santorini_freighter',
            numeric_id = 230,
            title = 'Santorini [Freighter]',
            capacity_pax = 0,
            capacity_cargo_holds = 960,
            capacity_mail = 0,
            capacity_special = [],
            replacement_id = '-none',
            buy_cost = 85,
            fixed_run_cost_factor = 7.0,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1953,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 1974], [1953, 9999]], {0: [0], 1953: [0, 1], 1974: [1]}],
            str_type_info = 'LARGE_COASTER',
            vehicle_life = 35,
            gross_tonnage = 960,
)
