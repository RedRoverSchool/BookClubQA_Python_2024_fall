
def test_main_page_info_is_same_after_reload(header, main_body, register):
    header.visit()
    main_page_info_before_reload = main_body.check_info_main_page()
    main_body.reload()
    main_page_info_after_reload = main_body.check_info_main_page()
    assert main_page_info_after_reload == main_page_info_before_reload
