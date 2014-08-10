import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'saint_marie_barge_tug',
            numeric_id = 2320,
            title = 'Saint Marie [Barge Tug]',
            capacity_cargo_holds = 200,
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 1.0,
            fuel_run_cost_factor = 1.0,
            speed = 16.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 87,
            loading_speed = 20,
            intro_date = 1870,
            buy_menu_bb_xy = [652, 28],
            str_type_info = 'BARGE_TUG',
            vehicle_life = 55,
            gross_tonnage = 45,
            graphics_status = 'Work in Progress - Coxx',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
