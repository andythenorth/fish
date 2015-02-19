import global_constants
from ship import UtilityVessel

ship = UtilityVessel(id = 'danube_utility_vessel',
            numeric_id = 2000,
            title = 'DANUBE [Utility Vessel]',
            capacity_pax = 36,
            capacity_cargo_holds = 24,
            capacity_mail = 30,
            replacement_id = '-none',
            buy_cost = 2,
            fixed_run_cost_factor = 1.5,
            fuel_run_cost_factor = 1.0,
            speed = 19.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 29,
            loading_speed = 15,
            intro_date = 1860,
            buy_menu_bb_xy = [673, 23],
            str_type_info = 'SMALL_GENERAL_PURPOSE_VESSEL',
            vehicle_life = 40,
            gross_tonnage = 30)

ship.add_model_variant(intro_date=0,
                       end_date=1945,
                       spritesheet_suffix=0)

ship.add_model_variant(intro_date=0,
                       end_date=1955,
                       spritesheet_suffix=1)

ship.add_model_variant(intro_date=0,
                       end_date=1955,
                       spritesheet_suffix=2)

ship.add_model_variant(intro_date=1930,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=3)
