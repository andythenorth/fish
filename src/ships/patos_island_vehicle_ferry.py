from ship import Ship, PacketBoat

ship = PacketBoat(id = 'patos_island_vehicle_ferry',
            numeric_id = 50,
            title = 'Patos Island [Ferry]',
            capacity_pax = 450,
            capacity_freight = 280,
            capacity_cargo_holds = 280,
            capacity_tanks = 0,
            capacity_mail = 360,
            capacity_special = [],
            default_cargo = 'PASS',
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 22.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-61, -28], [-36, -29], [-10, -28], [-14, -54], [-55, -26], [-36, -29], [0, -24]],
            buy_menu_width = 89,
            loading_speed = '35',
            intro_date = 1953,
            buy_menu_bb_xy = [622, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 60,
            custom_template = None,
            gross_tonnage = 500,
)
