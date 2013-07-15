from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'lindau_freight_barge',
            numeric_id = 210,
            title = 'Lindau [Freight Barge]',
            capacity_pax = 0,
            capacity_freight = 295,
            capacity_cargo_holds = 295,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [],
            replacement_id = '-none',
            buy_cost = 51,
            fixed_run_cost_factor = 4.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -54], [-63, -26], [-48, -21], [-11, -27], [-14, -54], [-65, -27], [-48, -21], [-12, -26]],
            buy_menu_width = 88,
            loading_speed = 20,
            intro_date = 1948,
            buy_menu_bb_xy = [624, 21],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            str_type_info = 'CARGO_VESSEL_INLAND',
            vehicle_life = 50,
            gross_tonnage = 300,
)
