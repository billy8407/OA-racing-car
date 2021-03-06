from setting.bet import BetDetails
from setting.function_wrapper import log_measure
from utility.fetch_handler import first_fetch
from utility.settings_handler import set_level, open_browser, user_login_prompt, check_login_page, set_backend_page, user_point_prompt
from utility.time_handler import check_service_time
from utility.processer_handler import start_processer

driver_list = []


def init():
    global driver_list
    bet_details = BetDetails()
    bet_details.level_list = set_level()

    driver = open_browser()

    user_login_prompt()
    check_login_page(driver)

    check_service_time()
    set_backend_page(driver)

    bet_details = user_point_prompt(bet_details)
    check_service_time()

    return bet_details, driver


@log_measure
def main():
    bet_details, driver = init()
    loop_queue, api_dic = first_fetch()
    start_processer(loop_queue, api_dic, bet_details, driver)

    driver.quit()


if __name__ == '__main__':
    main()
