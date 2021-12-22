## How to get around selenium blocking.
# Google no longer lets you use selenium to log into google.
#Following is the workaround.
# load package 'undetected_chromedriver.v2'


import undetected_chromedriver.v2 as uc
options = uc.ChromeOptions()
options.user_data_dir = 'C:\\temp\\profile'
options.add_argument('--user-data-dir=C:\\temp\\profile2')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

# The debug is a little annoying, and it closes the window whether it is successful or fails.
# Had to add input statements to get it to pause rather than closing windows when you can't tell what happened.