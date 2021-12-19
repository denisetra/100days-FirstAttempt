## Create a program that will auto-swipe in tinder.
## To avoid engaging anyone by accident, will choose 'dislike' instead of 'like'.
## Both Selenium and Tinder had significant changes from when the course was broadcasted
## Using "ActionChains" to swipe left resolved my issue.


from tinder import tinder_login, dislike_tinder


def main():
    tinder_login()
    dislike_tinder()

main()

