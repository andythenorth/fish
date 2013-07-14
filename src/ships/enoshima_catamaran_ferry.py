from ship import Ship, PacketBoat

ship = PacketBoat(id = 'enoshima_catamaran_ferry',
            numeric_id = '90',
            title = 'Enoshima [Fast Ferry]',
            capacity_pax = 300,
            capacity_freight = 175,
            capacity_cargo_holds = 175,
            capacity_tanks = 0,
            capacity_mail = 224,
            capacity_special = [],
            default_cargo = 'PASS',
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            speed = 50.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]],
            buy_menu_width = 67,
            loading_speed = '20',
            intro_date = 1997,
            buy_menu_bb_xy = [624, 28],
            graphic_variations_by_date = [[[1997, 9999], [1997, 9999]], {1997: [0, 1]}],
            graphics_template = 'default',
            str_type_info = 'CATAMARAN_FAST_FERRY',
            vehicle_life = 25,
            custom_template = None,
            gross_tonnage = 350,
)
