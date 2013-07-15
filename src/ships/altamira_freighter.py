from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'altamira_freighter',
            numeric_id = 190,
            title = 'Altamira [Freighter]',
            capacity_pax = 0,
            capacity_freight = 360,
            capacity_cargo_holds = 360,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [],
            default_cargo = 'COAL',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = '20',
            intro_date = 1900,
            buy_menu_bb_xy = [649, 21],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'COASTER',
            vehicle_life = 40,
            custom_template = None,
            gross_tonnage = 360,
)
