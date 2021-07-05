class Locators:
    # Login Page
    dd_login_menu_xpath = "//a[.='Sign in']//ancestor::li"
    input_username_id = "username-pulldown"
    input_password_id = "password-pulldown"
    btn_login_id = "login-pulldown"

    # Home Page
    link_sign_out_xpath = "//a[.='Sign out']"
    btn_new_project_xpath = "//*[@id='content']//a[contains(@title,'New project')]"
    dd_project_selector_xpath = "//*[@id='projects-menu']"
    dd_selected_project_xpath = "//a[.='{}']//ancestor::li[contains(@class,'menu-item')]"

    # New Project Page
    input_project_name_id = "formly_3_textInput_name_0"
    btn_advanced_settings_xpath = "//button[contains(text(),'Advanced settings')]"
    editor_project_desc_xpath = "//*[@id='formly_9_formattableInput_description_1']//p"
    dd_project_status_xpath = "//*[@id='formly_9_selectProjectStatusInput__links.status_4']"
    dd_project_selected_status_xpath = "//span[text()='{}']//parent::div"
    # dd_status_none_xpath = "//*[@id='formly_9_selectProjectStatusInput__links.status_4']//input"
    # dd_status_OnTrack_xpath = "//span[text()='On track']//parent::div"
    # dd_status_AtRisk_xpath = "//span[text()='At risk']//parent::div"
    # dd_status_OffTrack_xpath = "//span[text()='Off track']//parent::div"
    btn_save_project_xpath = "//button[@type='submit'][@class='button -highlight']"

    # Project Overview Page
    btn_project_name_xpath = "//*[@id='projects-menu']/span"
    dd_project_list_id = "ui-id-9"
    btn_menu_work_packages_id = "main-menu-work-packages-wrapper"

    # Work Packages Page
    dd_create_work_package_class = "wp-create-button"
    dd_create_task_xpath = "//*[@id='types-context-menu']//li[.='Task']"
    edit_work_package_type_class = "__hl_inline_type_1 inline-edit--display-field type -required -editable"
    edit_work_package_status_class = "inline-edit--display-field status -required -editable"
    # dd_actions_xpath = "//*[@id='wrapper']/header/div[1]/ul/li[2]"
    # dd_create_task_xpath = "//*[@id='quick-add-menu']//a[.='Task']"
    tb_work_packages_xpath = "//tbody[contains(@class,'results-tbody work-package--results-tbody')]//tr"
    tr_last_work_package_xpath = "//tbody[contains(@class,'results-tbody work-package--results-tbody')]//tr[last()]//span//span"
    form_new_task_class = "work-packages--details work-packages--new"
    input_task_subject_xpath = "//*[@id='wp-new-inline-edit--field-subject']"
    editor_task_desc_xpath = "//*[@class='op-uc-p']"
    btn_save_task_id = "work-packages--edit-actions-save"
    btn_back_xpath = "//*[@id='toolbar']/div/back-button"
    # btn_back_xpath = "//*[@id='menu-sidebar']/ul/li[2]/div[2]/a[2]"
    btn_back_class = "wp-show--back-button hide-when-print"
