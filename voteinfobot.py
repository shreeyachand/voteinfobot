# voteinfobot
import praw
import time
# not putting in the info for privacy reasons, but this is what the program needs to log in as the bot and do the automated reply
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')
# .hot(limit=100, skip_existing=True)
# phrases to activate the bot
keyphrase = ['Trump', 'trump', 'Biden', 'biden', 'mail-in', 'election', 'Election', ]
# r/politics doesn't actually allow for unauthorized bots to comment like this. 'politics' can be substituted for any valid subreddit, it was just way more likely that a keyword would be picked up in r/politics and so it was a good test for the bot, even if the actual comment wouldn't go through
for submission in reddit.subreddit('politics').stream.submissions(skip_existing=True):
    # look for phrase and reply appropriately
    if any(word in submission.title for word in keyphrase):
        reply = """**Vote in the 2020 Election on November 3rd.**

[Register yourself](https://www.usa.gov/register-to-vote)

[Find out if your state allows early in-person voting](https://www.axios.com/how-to-vote-by-state-2020-307c3d17-ee57-4a1b-8bad-182ca1cdb752.html) and [vote **as early as possible** in your state](https://www.vote.org/voter-registration-deadlines/)

[**Check your voter registration**](https://www.usa.gov/confirm-voter-registration)  regularly and encourage others to do the same

Drop off your ballot at a ballot drop off box or your local county elections office to avoid USPS uncertainty.

If you do return your ballot via mail, it is recommended to send it at least 1 week before November 3rd.

If you do not receive a ballot in the mail or you later change your mind to vote in person, then most states allow you to still vote in person!

[Sign up to become a **paid** poll worker!](https://www.eac.gov/help-america-vote)

^(I am a bot. I commented on this post because something in its title made me guess it was related to the 2020 election. If there is any more information you feel should be added or if you have any questions at all, please direct message me.)"""
        submission.reply(reply)
        print('posted')
        time.sleep(550)
    else:
        time.sleep(5)

print('done')
