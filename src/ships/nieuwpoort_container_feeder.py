from ship import Ship, FastFreighter

ship = FastFreighter(id = 'nieuwpoort_container_feeder',
            numeric_id = 300,
            title = 'Nieuwpoort [Container Feeder]',
            capacity_pax = 0,
            capacity_freight = 750,
            capacity_cargo_holds = 750,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [],
            default_cargo = 'GOOD',
            replacement_id = '-none',
            buy_cost = 58,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 119,
            loading_speed = '35',
            intro_date = 1979,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'CONTAINER_FEEDER',
            vehicle_life = 30,
            gross_tonnage = 800,
)
