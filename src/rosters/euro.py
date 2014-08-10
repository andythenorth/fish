from roster import Roster

from ships import constance_freight_barge
from ships import danube_large_ferry
from ships import danube_large_trawler
from ships import danube_livestock_barge
from ships import danube_paddle_steamer
from ships import danube_reefer
from ships import danube_small_ferry
from ships import danube_small_freight_barge
from ships import danube_trawler
from ships import danube_utility_vessel
from ships import danube_very_large_tanker
from ships import dieze_container_barge
from ships import endeavour_utility_catamaran
from ships import feodosiya_hydrofoil
from ships import geneva_freight_barge
from ships import saint_marie_barge_tug
from ships import volgoneft_six_thirty_tanker_barge
from ships import volgoneft_two_seventy_tanker_barge

roster = Roster(id = 'euro',
                buy_menu_sort_order = ['danube_utility_vessel',
                                       'danube_small_ferry',
                                       'danube_paddle_steamer',
                                       'danube_large_ferry',
                                       'feodosiya_hydrofoil',
                                       'danube_trawler',
                                       'danube_large_trawler',
                                       'endeavour_utility_catamaran',
                                       'danube_small_freight_barge',
                                       #'marstein_freighter',
                                       #'altamira_freighter',
                                       'saint_marie_barge_tug',
                                       'constance_freight_barge',
                                       'geneva_freight_barge',
                                       #'cadiz_freighter',
                                       #'frisco_bay_freighter',
                                       #'santorini_freighter',
                                       #'maspalomas_freighter',
                                       #'eddystone_tanker',
                                       #'hopetown_tanker',
                                       #'yokohama_tanker',
                                       'volgoneft_two_seventy_tanker_barge',
                                       'volgoneft_six_thirty_tanker_barge',
                                       'danube_very_large_tanker',
                                       'danube_reefer',
                                       'danube_livestock_barge',
                                       'dieze_container_barge'])
