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
    locator_status_selector_id = "formly_9_selectProjectStatusInput__links.status_4"
    locator_status_selector_class = "ng-input"
    locator_status_class = "ng-option"
    locator_status_classes = ["-on-track", "-at-risk", "-off-track"]
    locator_save_button_xpath = '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/div/button'

    ddStatus_xpath = "//body/div[@id='wrapper']/div[@id='main']/main[@id='content-wrapper']/div[@id='content']/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[5]/op-dynamic-field-wrapper[1]/op-form-field[1]/label[1]/div[3]/op-select-project-status-input[1]/ng-select[1]/div[1]/div[1]/div[3]/input[1]"
    ddStatus_relative_xpath = "//body[1]/div[2]/div[1]/main[1]/div[2]/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[5]/op-dynamic-field-wrapper[1]/op-form-field[1]/label[1]/div[3]/op-select-project-status-input[1]/ng-select[1]"
    ddStatusOnNone_xpath = "/ng-dropdown-panel[1]/div[1]/div[2]/div[0]"
    ddStatusOnTrack_xpath = '/html/body/div[2]/div[1]/main/div[2]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/div/formly-group/formly-field[5]/op-dynamic-field-wrapper/op-form-field/label/div[3]/op-select-project-status-input/ng-select/ng-dropdown-panel/div/div[2]/div[1]'
    ddStatusAtRisk_xpath = '/html/body/div[2]/div[1]/main/div[2]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/div/formly-group/formly-field[5]/op-dynamic-field-wrapper/op-form-field/label/div[3]/op-select-project-status-input/ng-select/ng-dropdown-panel/div/div[2]/div[2]'
    ddStatusOffTrack_xpath = "/ng-dropdown-panel[1]/div[1]/div[2]/div[3]"
    btnSaveNewProduct_xpath = "//button[@type='submit'][@class='button -highlight']"
