class TestLocators:
    # LoginPage
    locator_login_xpath = '//*[@id="wrapper"]/header/div[3]/ul/li[3]/a/span'
    locator_username_id = "username-pulldown"
    locator_password_id = "password-pulldown"
    locator_submit_id = "login-pulldown"

    # HomePage
    locator_avatar_alt = '[alt="A A"]'
    locator_new_project_button_xpath = "//*[@id='content']/section[1]/div[2]/div[2]/a[1]"

    # NewProjectPage
    locator_project_name_id = "formly_3_textInput_name_0"
    locator_advanced_settings_xpath = '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/legend/button'
    locator_description_text_xpath = '//*[@id="formly_9_formattableInput_description_1"]/div/op-ckeditor/div/div[2]/div'
    locator_status_selector_xpath = '//*[@id="formly_9_selectProjectStatusInput__links.status_4"]'
    ddStatusOnNone_xpath = "/ng-dropdown-panel[1]/div[1]/div[2]/div[0]"
    ddStatusOnTrack_xpath = '/html/body/div[2]/div[1]/main/div[2]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/div/formly-group/formly-field[5]/op-dynamic-field-wrapper/op-form-field/label/div[3]/op-select-project-status-input/ng-select/ng-dropdown-panel/div/div[2]/div[1]'
    ddStatusAtRisk_xpath = '/html/body/div[2]/div[1]/main/div[2]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/div/formly-group/formly-field[5]/op-dynamic-field-wrapper/op-form-field/label/div[3]/op-select-project-status-input/ng-select/ng-dropdown-panel/div/div[2]/div[2]'
    ddStatusOffTrack_xpath = "/ng-dropdown-panel[1]/div[1]/div[2]/div[3]"
    btnSaveNewProduct_xpath = "//button[@type='submit'][@class='button -highlight']"
    locator_save_button_xpath = '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/div/button'

    # WorkPackagesPage
    locator_project_selector_xpath = '//*[@id="projects-menu"]/span'
    locator_project_list_id = "ui-id-1"

    # ProjectOverViewPage
