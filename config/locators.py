class TestLocators:
    # LoginPage
    locator_username_id = "username"
    locator_password_id = "password"
    locator_submit_xpath = '//*[@id="login-form"]/form/input[4]'
    locator_submit_name = "Sign in"

    # HomePage
    locator_new_project_button_xpath = "//*[@id='content']/section[1]/div[2]/div[2]/a[1]"

    # NewProjectPage
    locator_project_name_id = "formly_3_textInput_name_0"
    locator_advanced_settings_xpath = '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/legend/button'
    locator_description_text_xpath = '//*[@id="formly_9_formattableInput_description_1"]/div/op-ckeditor/div/div[2]/div'
    locator_status_selector_xpath = '//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input'
    locator_status_selector_id = "formly_9_selectProjectStatusInput__links.status_4"
    locator_status_selector_class = "ng-input"
    locator_status_class = "ng-option"
    locator_save_button_xpath = '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/div/button'
