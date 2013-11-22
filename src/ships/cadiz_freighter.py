import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'cadiz_freighter',
            numeric_id = 170,
            title = 'Cadiz [Freighter]',
            capacity_cargo_holds = 450,
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 109,
            loading_speed = 20,
            intro_date = 1970,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'COASTER',
            vehicle_life = 40,
            gross_tonnage = 360,
            vehicle_groups = ['sea'], 
            graphics_status = 'Work in Progress - Coxx',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
