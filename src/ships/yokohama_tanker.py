from ship import Ship, Tanker

ship = Tanker(id = 'yokohama_tanker',
            numeric_id = 280,
            title = 'Yokohama [Tanker]',
            capacity_pax = 0,
            capacity_freight = 1220,
            capacity_cargo_holds = 0,
            capacity_tanks = 1220,
            capacity_mail = 0,
            capacity_special = [],
            default_cargo = 'OIL_',
            replacement_id = '-none',
            buy_cost = 99,
            fixed_run_cost_factor = 8.0,
            fuel_run_cost_factor = 1.0,
            speed = 22.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = '40',
            intro_date = 1973,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'tanker',
            str_type_info = 'LARGE_COASTAL_TANKER',
            vehicle_life = 45,
            custom_template = None,
            gross_tonnage = 1290,
)
